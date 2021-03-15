import random
import math
import itertools import product
from multiprocessing import Process, Value, Array, Manager

class ReverseBJL:
    """
    百家樂模擬 version 1
    很多排組 一個切牌位置 
    """

    def __init__(self):
        pass

    def generateCardset(self, setNumber=8):
        # 創造牌組
        # 花色, 號碼
        colors = list(map(lambda ele: str(ele), range(1, 5)))
        numbers = list(map(lambda ele: str(ele), range(1, 14)))

        cards = []

        # 迴圈造牌
        for color in colors:
            cards += map(lambda ele: '-'.join([color, ele]), numbers)

        # 變成 8 副牌
        cards = cards * setNumber
        return cards

    def shuffleCard(self, cardset):
        # 洗牌
        shuffledCards = random.sample(cardset, 416)
        return shuffledCards

    def getNumber(self, card):
        # 撲克牌點數 -> 百家樂點數
        return 10 if (int(card[2:])) // 10 else int(card[2:])

    def getPoint(self, cards):
        # 計算手牌點數
        point = sum([self.getNumber(ele) for ele in cards]) % 10
        return point

    def randPop(self, cardset):
        # 隨機挑牌
        if len(cardset) > 2:
            return cardset.pop(random.randint(1, len(cardset)-1))
        else:
            return cardset.pop()

    def pointAfterAdd(self, pointBefore, addedCard):
        # 計算補牌後點數
        return (pointBefore + self.getNumber(addedCard)) % 10

    def randomBuild(self, maxLength=6, singleJumpTimes=0, singleJumpMax=4, doubleJumpTimes=0, doubleJumpMax=4):
        """
        1. maxLength: 最高長龍
        2. singleJumpTimes: 單跳出現的次數
        3. singleJumpMax: 單跳最高長度
        4. doubleJumpTimes: 雙跳出現的次數
        5. doubleJumpTimes: 雙跳最高長度
        """
        # 創造排組, 洗牌增加隨機性
        cards = self.shuffleCard(self.generateCardset())

        result = []  # 存花色點數
        rounds = []
        details = []

        if singleJumpTimes or doubleJumpTimes:
            # 組合最終結果
            betweenLen = [random.randint(1, 7) for _ in range(
                singleJumpTimes + doubleJumpTimes)]
            frontLen = random.randint(1, 5)
            backLen = 15

            # shuffle single double array
            potentials = [1] * singleJumpTimes + [2] * doubleJumpTimes
            addedLen = random.sample(potentials, len(potentials))

            # 備用 list
            allRange = list(range(1, maxLength+1))
            noSingle = list(filter(lambda ele: ele != 1, allRange))
            noDouble = list(filter(lambda ele: ele != 2, allRange))

            # 組合
            frontLists = [random.randint(1, maxLength)
                          for _ in range(frontLen-1)]
            betweenLists = []
            for pattern in addedLen:
                temp = []
                target = singleJumpMax if pattern == 1 else doubleJumpMax
                temp.append(random.choice(
                    noSingle if pattern == 1 else noDouble))
                temp += [pattern] * \
                    (random.randint(4, target) if target != 4 else 4)
                temp.append(random.choice(
                    noSingle if pattern == 1 else noDouble))
                temp += [random.randint(1, maxLength)
                         for _ in range(betweenLen.pop())]
                betweenLists += temp

            # 最終結果
            numRounds = frontLists + betweenLists + \
                [random.randint(1, maxLength) for _ in range(backLen)]

        else:
            numRounds = [random.randint(1, maxLength) for _ in range(25)]

        # 決定第一長龍的贏家
        currentWinner = random.choice(['庄', '閑'])

        # 重建群組, 直到牌無法成局
        while len(cards) >= 6 and numRounds:

            # 取得長龍長度
            longCount = numRounds.pop(0)

            # 組建每局牌的無限迴圈
            while longCount > 0:

                # 在牌組張數不足 6 不成局時, 結束無限迴圈
                if len(cards) < 6:
                    break

                player = []  # 存單局 閑 牌組
                banker = []  # 存單局 庄 牌組

                popIndex = [self.randPop(cards) for _ in range(4)]

                # 隨機發 4 張牌
                while popIndex:
                    if popIndex:
                        player.append(popIndex.pop())
                    if popIndex:
                        banker.append(popIndex.pop())

                # 計算前 2 張點數
                playerPoint = self.getPoint(player)
                bankerPoint = self.getPoint(banker)

                # 判斷 閑 是否補牌
                doPlayerAddCard = playerPoint < 6

                # 補牌規則
                # 閑家只要小於6 就補牌
                if doPlayerAddCard:
                    playerAddCard = self.randPop(cards)
                    playerPoint = self.pointAfterAdd(
                        playerPoint, playerAddCard)
                    player.append(playerAddCard)

                # 莊家補牌規則
                # 莊家 > 6: 不補牌
                if bankerPoint <= 6:
                    if bankerPoint == 6:     # 莊家 = 6
                        if doPlayerAddCard:  # 閒家補排
                            if playerPoint in [6, 7]:  # 閒家補牌後點數: 6, 7 -> 補牌
                                bankerAddCard = self.randPop(cards)
                                bankerPoint = self.pointAfterAdd(
                                    bankerPoint, bankerAddCard)
                                banker.append(bankerAddCard)

                    elif bankerPoint == 5:   # 莊家 = 5:
                        if doPlayerAddCard:  # 閒家補牌
                            if playerPoint in [4, 5, 6, 7]:  # 閒家補牌後點數: 4, 5, 6, 7 -> 補牌
                                bankerAddCard = self.randPop(cards)
                                bankerPoint = self.pointAfterAdd(
                                    bankerPoint, bankerAddCard)
                                banker.append(bankerAddCard)

                        else:   # 閒家不補牌, 莊家直接補牌
                            bankerAddCard = self.randPop(cards)
                            bankerPoint = self.pointAfterAdd(
                                bankerPoint, bankerAddCard)
                            banker.append(bankerAddCard)

                    elif bankerPoint == 4:  # 莊家 = 4
                        if doPlayerAddCard:  # 閒家補牌
                            # 閒家補牌後點數:0,1,8,9 -> 補牌
                            if playerPoint not in [0, 1, 8, 9]:
                                bankerAddCard = self.randPop(cards)
                                bankerPoint = self.pointAfterAdd(
                                    bankerPoint, bankerAddCard)
                                banker.append(bankerAddCard)

                        else:  # 閒家不補牌, 莊家直接補牌
                            bankerAddCard = self.randPop(cards)
                            bankerPoint = self.pointAfterAdd(
                                bankerPoint, bankerAddCard)
                            banker.append(bankerAddCard)

                    elif bankerPoint == 3:  # 莊家 = 3
                        if doPlayerAddCard:
                            if playerPoint != 8:  # 閒家補牌後點數只要不為 8 -> 補牌
                                bankerAddCard = self.randPop(cards)
                                bankerPoint = self.pointAfterAdd(
                                    bankerPoint, bankerAddCard)
                                banker.append(bankerAddCard)

                        else:  # 閒家不補牌, 莊家直接補牌
                            bankerAddCard = self.randPop(cards)
                            bankerPoint = self.pointAfterAdd(
                                bankerPoint, bankerAddCard)
                            banker.append(bankerAddCard)

                    else:  # 莊家 <= 2, 直接補牌
                        bankerAddCard = self.randPop(cards)
                        bankerPoint = self.pointAfterAdd(
                            bankerPoint, bankerAddCard)
                        banker.append(bankerAddCard)

                # 確認贏家
                winner = "閑" if playerPoint > bankerPoint else "和" if playerPoint == bankerPoint else "庄"

                # 如果和局, 用 1:9 決定是否保留 (留:1, 去:9)
                canBeEven = False
                if winner == "和":
                    canBeEven = random.choices([True, False], [30, 50])[0]

                if winner == currentWinner or canBeEven:
                    rounds.append(winner)
                    details.append({
                        'player': player.copy(),
                        'banker': banker.copy(),
                        'winner': winner,
                    })

                    # 和局 longCount 不減1
                    if not canBeEven:
                        longCount -= 1

                    for i in range(3):
                        if player:
                            result.append(player.pop(0))
                        if banker:
                            result.append(banker.pop(0))

                else:
                    cards.extend(player)
                    cards.extend(banker)

                if longCount == 0:
                    if numRounds:
                        longCount = numRounds.pop(0)
                        currentWinner = "庄" if currentWinner == "閑" else "閑"
                    else:
                        break

        return result, rounds, cards, details

    def reverseCut(self, cardsets, position):
        # 回復切牌前結果
        frontPart = cardsets[(-1 * position):]
        endPart = cardsets[: (-1 * position)]
        return frontPart + endPart

class BJLVer2:
    colors = [str(ele) for ele in range(1, 5)]
    numbers = [str(ele) for ele in range(1, 14)]

    all_cards = ['-'.join(ele) for ele in product(colors, numbers)] * 8

    # def __init__(self):
    # self.shuffled = self.shuffledCards()

    def shuffledCards(self):
        """
        洗牌功能
        """
        shuffledCards = random.sample(self.all_cards, 416)
        return shuffledCards

    def cutCards(self, shuffled, position):
        """
        切牌功能
        """
        return shuffled[position:] + shuffled[:position]
        # return self.shuffled[position:] + self.shuffled[:position]

    def getNumber(self, card):
        """
        計算單張牌的點數
        """
        return 10 if (int(card[2:])) // 10 else int(card[2:])

    def getPoint(self, cards):
        """
        計算牌組點數
        """
        point = sum([self.getNumber(ele) for ele in cards]) % 10
        return point

    def pointAfterAdd(self, pointBefore, addedCard):
        """
        計算補牌後點數
        pointBefore: 補牌前點數
        addedCard: 補牌
        """
        return (pointBefore + self.getNumber(addedCard)) % 10

    def getWinner(self, player, banker, backup):
        """
        計算當局贏家
        player: 閑家補牌前牌組
        banker: 莊家補牌前牌組
        backup: 補牌牌組
        """

        playerPoint = self.getPoint(player)
        bankerPoint = self.getPoint(banker)

        # 判斷 閑家 是否須要補牌
        doPlayerAddCard = playerPoint < 6

        # 補排規則
        # 閑家只要小於 6 就要補牌
        if doPlayerAddCard:
            playerAddCard = backup.pop(0)
            playerPoint = self.pointAfterAdd(playerPoint, playerAddCard)
            player.append(player.append(playerAddCard))

        # 莊家補牌規則
        # 莊家 > 6: 不補牌
        if bankerPoint <= 6:
            if bankerPoint == 6:       # 莊家 = 6
                if doPlayerAddCard:    # 閑家補牌
                    if playerPoint in [6, 7]:  # 閒家補牌後點數: 6, 7 -> 補牌
                        bankerAddCard = backup.pop(0)
                        bankerPoint = self.pointAfterAdd(
                            bankerPoint, bankerAddCard)
                        banker.append(bankerAddCard)

            elif bankerPoint == 5:     # 莊家 = 5:
                if doPlayerAddCard:    # 閒家補牌
                    if playerPoint in [4, 5, 6, 7]:  # 閒家補牌後點數: 4, 5, 6, 7 -> 補牌
                        bankerAddCard = backup.pop(0)
                        bankerPoint = self.pointAfterAdd(
                            bankerPoint, bankerAddCard)
                        banker.append(bankerAddCard)
                else:     # 閒家不補牌, 莊家直接補牌
                    bankerAddCard = backup.pop(0)
                    bankerPoint = self.pointAfterAdd(
                        bankerPoint, bankerAddCard)
                    banker.append(bankerAddCard)

            elif bankerPoint == 4:  # 莊家 = 4
                if doPlayerAddCard:  # 閑家補牌
                    if playerPoint not in [0, 1, 8, 9]:   # 閒家補牌後點數:0,1,8,9 -> 補牌
                        bankerAddCard = backup.pop(0)
                        bankerPoint = self.pointAfterAdd(
                            bankerPoint, bankerAddCard)
                        banker.append(bankerAddCard)
                else:  # 閑家不補牌, 莊家直接補牌
                    bankerAddCard = backup.pop(0)
                    bankerPoint = self.pointAfterAdd(
                        bankerPoint, bankerAddCard)
                    banker.append(bankerAddCard)

            elif bankerPoint == 3:  # 莊家 = 3
                if doPlayerAddCard:
                    if playerPoint != 8:
                        bankerAddCard = backup.pop(0)
                        bankerPoint = self.pointAfterAdd(
                            bankerPoint, bankerAddCard)
                        banker.append(bankerAddCard)
                else:  # 閒家不補牌, 莊家直接補牌
                    bankerAddCard = backup.pop(0)
                    bankerPoint = self.pointAfterAdd(
                        bankerPoint, bankerAddCard)
                    banker.append(bankerAddCard)

            else:  # 莊家 <= 2 直接補牌
                bankerAddCard = backup.pop(0)
                bankerPoint = self.pointAfterAdd(bankerPoint, bankerAddCard)
                banker.append(bankerAddCard)

        # 確認贏家
        winner = "閑" if playerPoint > bankerPoint else "和" if playerPoint == bankerPoint else "庄"

        return winner, player, banker, backup

    def getRoad(self, cards):
        """
        計算開出輸贏結果路詳細情況
        cardSets: 切牌後牌組
        """
        cardSets = cards.copy()
        rounds = []

        while len(cardSets) > 6:

            playerCards = []
            bankerCards = []
            backupCards = []

            while len(playerCards) < 2 and len(bankerCards) < 2:
                playerCards.append(cardSets.pop(0))
                bankerCards.append(cardSets.pop(0))

            for _ in range(2):
                backupCards.append(cardSets.pop(0))
            try:
                winner, playerCards, bankerCards, backupCards = self.getWinner(
                    playerCards, bankerCards, backupCards)
            except:
                print("cards: ", cards)
                print("cardSets: ", cardSets)
                print("playerCard: ", playerCards)
                print('bankerCard: ', bankerCards)
                print('backupCards: ', backupCards)

            rounds.append(winner)
            # rounds.append({
            #     'player': playerCards,
            #     'banker': bankerCards,
            #     'winner': winner,
            # })

            if len(backupCards) > 0:
                cards = backupCards + cards

        return rounds

    def getStatic(self, rou):

        # rounds = [ele['winner'] for ele in rou]
        rounds = rou.copy()

        currX = 1
        currY = 1
        maxLWE = 1
        result = []

        maxSingleJump = 0  # 最長單跳
        maxDoubleJump = 0  # 最長雙跳

        # 取得第一個非 "和" 的值
        firstNotEven = list(filter(lambda ele: ele != "和", rounds))[0]

        # 取得第一個值
        currRecord = rounds.pop(0)

        # 長龍起始計算值, 如果第一個值是和需要從0計算
        maxLWE = 0 if currRecord == "和" else 1
        maxY = 1

        # 紀錄每個值的轉換座標和顏色
        tempRecord = {
            'x': currX,
            'y': currY,
            'result': currRecord,
            'fill': 'red' if currRecord == "閑" else "blue" if currRecord == "庄" else 'green'
        }

        # 存回 result
        result.append(tempRecord)

        currLWE = 0 if currRecord == "和" else 1  # 紀錄單一路無和長度

        # 避免第一結果是 “和”
        # 指定為第一個非何得值
        if currRecord == "和":
            currRecord = firstNotEven
            currLWE = 0

        singleJump = 0  # 紀錄連續出現 1 長度
        doubleJump = 0  # 紀錄連續出現 2 長度

        while rounds:
            prevRecord = currRecord
            currRecord = rounds.pop(0)

            # 後者不等於前者｜和
            if currRecord not in [prevRecord, "和"]:

                # 換路
                currX += 1

                if currY > maxY:
                    maxY = currY

                currY = 1

                # 檢查前者是否為 單跳
                if currLWE != 1:
                    if singleJump > maxSingleJump:
                        maxSingleJump = singleJump
                    singleJump = 0
                else:
                    singleJump += 1

                # 檢查雙跳
                if currLWE != 2:
                    if doubleJump > maxDoubleJump:
                        maxDoubleJump = doubleJump
                    doubleJump = 0
                else:
                    doubleJump += 1

                # 檢查最長龍
                if currLWE > maxLWE:
                    maxLWE = currLWE

                # 非和 長龍計算器歸 0
                currLWE = 1

            else:
                # 現值 == "和" or 前值
                # y 值 + 1 x不變
                currY += 1

                # 如果非和, 長龍計算器＋1
                if currRecord != "和":
                    currLWE += 1

            result.append({
                'x': currX,
                'y': currY,
                'result': currRecord,
                'fill': 'red' if currRecord == "閑" else "blue" if currRecord == "庄" else 'green'
            })

        return {
            'result': result,
            'static': {'maxLWE': maxLWE, 'maxY': maxY, 'maxX': currX, 'maxSingleJump': maxSingleJump, 'maxDoubleJump': maxDoubleJump}
        }

    def roadLoop(self, longLen=None, maxSingleLen=None, maxDoubleLen=None, cutStart=150, cutEnd=280):

        # 洗牌
        shuffled = self.shuffledCards()

        # 迴圈跑切排算路
        result = {'roads': {}}
        maxX = 1
        maxY = 1

        matched = []

        for pos in range(cutStart, cutEnd+1):

            cuttedCard = self.cutCards(shuffled, pos)
            roads = self.getRoad(cuttedCard)
            maps = self.getStatic(roads)
            result['roads'][str(pos)] = {'road': roads, 'maps': maps}

            maxX = maps['static']['maxX'] if maps['static']['maxX'] > maxX else maxX
            maxY = maps['static']['maxY'] if maps['static']['maxY'] > maxY else maxY

            if longLen:
                longCheck = maps['static']['maxLWE'] <= longLen
            else:
                longCheck = True

            if maxSingleLen:
                singleCheck = maps['static']['maxSingleJump'] <= maxSingleLen
            else:
                singleCheck = True

            if maxDoubleLen:
                doubleCheck = maps['static']['maxSingleJump'] <= maxDoubleLen
            else:
                doubleCheck = True

            if longCheck and singleCheck and doubleCheck:
                matched.append(pos)

        result['maxX'] = maxX
        result['maxY'] = maxY
        result['rate'] = len(matched)/(cutEnd-cutStart+1)
        result['gCount'] = len(matched)
        result['matched'] = matched
        result['realCard'] = shuffled

        return result

    def getMultiSets(self, n=10, longLen=None, maxSingleLen=None, maxDoubleLen=None, okRate=0.5, cutStart=150, cutEnd=280):
        """
        迴圈取得 10 副可用牌組的功能
        n: 要取得幾副牌
        longLen: 長龍最高長度
        maxSingleLen: 單跳連續次數
        maxDoubleLen: 雙跳連續次數
        """
        allSets = {}
        t = 0
        while t < 10:
            roadData = self.roadLoop(
                longLen=longLen, maxSingleLen=maxSingleLen, maxDoubleLen=maxDoubleLen, cutStart=cutStart, cutEnd=cutEnd)
            if roadData['rate'] >= okRate:
                allSets['A' + str(t)] = roadData
                t += 1

        return allSets

    def getMultiSetsNS(self, checkStop, allSets, longLen=None, maxSingleLen=None, maxDoubleLen=None, okRate=0.5, cutStart=150, cutEnd=280):
        """
        取得符合條件牌組的無限迴圈
        n: 要取得幾副牌
        longLen: 長龍最高長度
        maxSingleLen: 單跳連續次數
        maxDoubleLen: 雙跳連續次數
        """
        t = 1

        while checkStop.value:
            roadData = self.roadLoop(
                longLen=longLen, maxSingleLen=maxSingleLen, maxDoubleLen=maxDoubleLen, cutStart=cutStart, cutEnd=cutEnd)
            if roadData['rate'] >= okRate:
                allSets['A' + str(t)] = roadData
                t += 1

            if len(allSets.keys()) == 25:
                checkStop.value = False

    def getMultiSetsWithTO(self, longLen=None, maxSingle=None, maxDouble=None, okRate=0.5, cutStart=150, cutEnd=280):
        """
        設定 迴圈運行時間
        """
        manager = Manager()

        allSet = manager.dict()
        checkStop = manager.Value('I', True)

        paras = {
            'checkStop': checkStop,
            'allSets': allSet,
            'longLen': longLen,
            'maxSingleLen': maxSingle,
            'maxDoubleLen': maxDouble,
            'okRate': okRate,
            'cutStart': cutStart,
            'cutEnd': cutEnd
        }

        p = Process(
            target=self.getMultiSetsNS,
            kwargs=paras)

        p.start()
        p.join(timeout=10)
        p.terminate()

        if p.exitcode is None:
            checkStop.value = False
            return dict(allSet)

        if p.exitcode == 0:
            return dict(allSet)
        return dict(allSet)
