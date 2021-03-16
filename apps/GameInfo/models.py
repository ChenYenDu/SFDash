# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApikeyListName(models.Model):
    apikey = models.CharField(db_column='APIKey', unique=True, max_length=16, blank=True, null=True)  # Field name made lowercase.
    apiname = models.CharField(db_column='APIName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apikey_list_name'


class CtlLog(models.Model):
    mode = models.PositiveIntegerField()
    type = models.CharField(max_length=30)
    text = models.TextField()
    user = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ctl_log'


class GameAd(models.Model):
    name = models.CharField(max_length=100)
    links = models.CharField(max_length=300)
    img = models.CharField(max_length=300, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_ad'


class GameBjl(models.Model):
    gameid = models.CharField(max_length=20, blank=True, null=True)
    period = models.CharField(db_column='Period', max_length=16)  # Field name made lowercase.
    kl8number = models.CharField(db_column='KL8Number', max_length=80)  # Field name made lowercase.
    setnumber = models.CharField(db_column='SetNumber', max_length=80)  # Field name made lowercase.
    pokerpoint = models.CharField(db_column='PokerPoint', max_length=45)  # Field name made lowercase.
    before = models.TextField(db_column='Before')  # Field name made lowercase.
    after = models.TextField(db_column='After')  # Field name made lowercase.
    status = models.IntegerField()
    lottime = models.DateTimeField(db_column='LotTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game_bjl'


class GameBuylist(models.Model):
    buyid = models.CharField(max_length=45)
    betlogid = models.PositiveIntegerField(db_column='BetLogID')  # Field name made lowercase.
    errorcode = models.IntegerField(db_column='ErrorCode')  # Field name made lowercase.
    errormsg = models.CharField(db_column='ErrorMsg', max_length=250)  # Field name made lowercase.
    errorcodep = models.IntegerField(db_column='ErrorCodeP')  # Field name made lowercase.
    errormsgp = models.CharField(db_column='ErrorMsgP', max_length=250)  # Field name made lowercase.
    userid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    location = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    playkey = models.CharField(max_length=20, blank=True, null=True)
    list_id = models.CharField(max_length=30, blank=True, null=True)
    period = models.CharField(max_length=30, blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    nums = models.IntegerField(blank=True, null=True)
    times = models.DecimalField(max_digits=13, decimal_places=2)
    pri_mode = models.CharField(max_length=8, blank=True, null=True)
    pri_number = models.CharField(max_length=65, blank=True, null=True)
    modes = models.CharField(max_length=12, blank=True, null=True)
    modetype = models.CharField(db_column='ModeType', max_length=6, blank=True, null=True)  # Field name made lowercase.
    prize_date = models.IntegerField()
    pri_money = models.CharField(max_length=16, blank=True, null=True)
    money = models.CharField(max_length=20, blank=True, null=True)
    super_money = models.CharField(max_length=16, blank=True, null=True)
    super_status = models.IntegerField(blank=True, null=True)
    is_zuih = models.CharField(max_length=5, blank=True, null=True)
    is_succeed = models.CharField(max_length=5, blank=True, null=True)
    is_ok = models.CharField(max_length=5, blank=True, null=True)
    is_zuih_pri_stop = models.SmallIntegerField(blank=True, null=True)
    z_number = models.CharField(max_length=10, blank=True, null=True)
    prizenum = models.CharField(max_length=3, blank=True, null=True)
    prize_time = models.DateTimeField(blank=True, null=True)
    isprize = models.CharField(max_length=12, blank=True, null=True)
    pri_other = models.CharField(max_length=16, blank=True, null=True)
    rebate_buy = models.CharField(max_length=5, blank=True, null=True)
    rebate_last_num = models.CharField(max_length=5, blank=True, null=True)
    rebate_list = models.CharField(max_length=1000, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    lottery_rate = models.CharField(max_length=15)
    gstatus = models.SmallIntegerField(db_column='gStatus', blank=True, null=True)  # Field name made lowercase.
    msystem = models.CharField(db_column='mSystem', max_length=30)  # Field name made lowercase.
    score = models.IntegerField()
    selfpoint = models.CharField(max_length=20, blank=True, null=True)
    experience = models.CharField(max_length=1)
    sys_mode = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    z_notopen = models.CharField(max_length=8, blank=True, null=True)
    field_is_latest_rate = models.CharField(db_column='\x08is_latest_rate', max_length=1)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    z_buy_rate = models.CharField(max_length=60, blank=True, null=True)
    buy_rate = models.CharField(max_length=20)
    z_set_num = models.TextField()
    handicaps = models.CharField(max_length=1)
    currency = models.CharField(max_length=5, blank=True, null=True)
    currency_diff = models.CharField(max_length=10, blank=True, null=True)
    afterpoints = models.DecimalField(max_digits=15, decimal_places=6)
    up6_id = models.IntegerField()
    up6_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up6_war = models.DecimalField(max_digits=5, decimal_places=2)
    up6_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up6_result = models.DecimalField(max_digits=15, decimal_places=6)
    up5_id = models.IntegerField()
    up5_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up5_war = models.DecimalField(max_digits=5, decimal_places=2)
    up5_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up5_result = models.DecimalField(max_digits=15, decimal_places=6)
    up4_id = models.IntegerField()
    up4_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up4_war = models.DecimalField(max_digits=5, decimal_places=2)
    up4_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up4_result = models.DecimalField(max_digits=15, decimal_places=6)
    up3_id = models.IntegerField()
    up3_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up3_war = models.DecimalField(max_digits=5, decimal_places=2)
    up3_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up3_result = models.DecimalField(max_digits=15, decimal_places=6)
    up2_id = models.IntegerField()
    up2_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up2_war = models.DecimalField(max_digits=5, decimal_places=2)
    up2_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up2_result = models.DecimalField(max_digits=15, decimal_places=6)
    up1_id = models.IntegerField()
    up1_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up1_war = models.DecimalField(max_digits=5, decimal_places=2)
    up1_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up1_result = models.DecimalField(max_digits=15, decimal_places=6)
    up0_id = models.IntegerField()
    up0_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up0_war = models.DecimalField(max_digits=5, decimal_places=2)
    up0_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up0_result = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'game_buylist'


class GameBuytemp(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    buyid = models.CharField(unique=True, max_length=45, blank=True, null=True)
    list_id = models.CharField(max_length=30, blank=True, null=True)
    money = models.CharField(max_length=30, blank=True, null=True)
    gametype = models.CharField(db_column='GameType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    betpointst = models.CharField(db_column='BetPointst', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commrate = models.CharField(db_column='CommRate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    moneymode = models.CharField(db_column='MoneyMode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    betcontent = models.TextField(db_column='BetContent', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_buytemp'


class GameCode(models.Model):
    fullname = models.CharField(max_length=60, blank=True, null=True)
    fullname_tw = models.CharField(max_length=60, blank=True, null=True)
    ckey = models.CharField(max_length=30, blank=True, null=True)
    cate = models.CharField(max_length=30, blank=True, null=True)
    codelist = models.CharField(max_length=400, blank=True, null=True)
    mode = models.CharField(max_length=8, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_code'


class GameCodeList(models.Model):
    codekey = models.CharField(db_column='CodeKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    listkey = models.CharField(db_column='ListKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    showtile = models.CharField(db_column='ShowTile', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codetile = models.CharField(db_column='CodeTile', max_length=30, blank=True, null=True)  # Field name made lowercase.
    showtile_tw = models.CharField(db_column='ShowTile_tw', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codetile_tw = models.CharField(db_column='CodeTile_tw', max_length=30, blank=True, null=True)  # Field name made lowercase.
    orders = models.SmallIntegerField(db_column='OrderS', blank=True, null=True)  # Field name made lowercase.
    rebate = models.CharField(db_column='Rebate', max_length=8, blank=True, null=True)  # Field name made lowercase.
    maxnote = models.CharField(db_column='MaxNote', max_length=8, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    apikey = models.CharField(db_column='APIKey', max_length=16, blank=True, null=True)  # Field name made lowercase.
    apikey2 = models.CharField(db_column='APIKey2', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game_code_list'


class GameDelay(models.Model):
    week = models.IntegerField()
    playkey = models.CharField(max_length=30)
    hasweek = models.CharField(max_length=15)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_delay'


class GameDtmode(models.Model):
    playkey = models.CharField(max_length=45, blank=True, null=True)
    skey = models.CharField(max_length=45, blank=True, null=True)
    limitnums = models.IntegerField()
    limitmoney = models.CharField(max_length=16)
    status = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_dtmode'
        unique_together = (('playkey', 'skey'),)


class GameJumpSetting(models.Model):
    playkey = models.CharField(max_length=45)
    codekey = models.CharField(max_length=45)
    listkey = models.CharField(max_length=45)
    buycount = models.IntegerField()
    pluscount = models.IntegerField()
    jumpsetnum = models.CharField(max_length=11)
    nopensetnum = models.CharField(max_length=11)
    linktime = models.IntegerField()
    buydownmax = models.IntegerField()
    linkdownmax = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_jump_setting'


class GameKinds(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    skey = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    title_tw = models.CharField(max_length=255, blank=True, null=True)
    change_rate = models.FloatField()
    returns = models.IntegerField(db_column='returnS')  # Field name made lowercase.
    extra = models.IntegerField()
    enable = models.IntegerField()
    rp_alter = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_kinds'


class GameLimitLhc(models.Model):
    playkey = models.CharField(max_length=20)
    codeid = models.CharField(max_length=20)
    playid = models.CharField(max_length=30)
    limitnum = models.TextField()
    limitrate = models.CharField(max_length=20)
    limitperiod = models.CharField(max_length=20)
    limittype = models.IntegerField()
    limithandicaps = models.CharField(max_length=10)
    limitstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'game_limit_lhc'


class GameLimitPk(models.Model):
    list_id = models.CharField(max_length=30, blank=True, null=True)
    limitnums = models.IntegerField(db_column='limitNums', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_limit_pk'


class GameLimitSetting(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    limitmoney = models.CharField(db_column='limitMoney', max_length=16, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_limit_setting'


class GameLimitTimes(models.Model):
    forgames = models.CharField(db_column='ForGames', max_length=20, blank=True, null=True)  # Field name made lowercase.
    forplays = models.CharField(db_column='ForPlays', max_length=20, blank=True, null=True)  # Field name made lowercase.
    forusers = models.CharField(db_column='ForUsers', max_length=10, blank=True, null=True)  # Field name made lowercase.
    forrange = models.SmallIntegerField(db_column='ForRange', blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(max_length=10, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_limit_times'


class GameLimitUser(models.Model):
    user_id = models.IntegerField()
    playkey = models.CharField(max_length=8)
    codekey = models.CharField(max_length=20)
    choose = models.IntegerField()
    sin_per = models.IntegerField()
    sin_zhu = models.IntegerField()
    status = models.IntegerField()
    updated_user = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_limit_user'


class GameLottery(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    playkey = models.CharField(db_column='playKey', max_length=10, blank=True, null=True)  # Field name made lowercase.
    serialid = models.CharField(db_column='SerialID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    serialdate = models.CharField(db_column='SerialDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(max_length=16, blank=True, null=True)
    number = models.CharField(db_column='Number', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lottime = models.DateTimeField(db_column='LotTime', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(blank=True, null=True)
    wrongcheck = models.IntegerField()
    keyinuser = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'game_lottery'


class GameLotteryStatus(models.Model):
    playkey = models.CharField(db_column='playKey', max_length=16, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(max_length=16, blank=True, null=True)
    lastperiod = models.CharField(db_column='LastPeriod', max_length=16, blank=True, null=True)  # Field name made lowercase.
    lastnumber = models.CharField(db_column='LastNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lottime = models.DateTimeField(db_column='LotTime', blank=True, null=True)  # Field name made lowercase.
    update_at = models.DateTimeField(blank=True, null=True)
    failtime = models.IntegerField(blank=True, null=True)
    modes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_lottery_status'


class GameLotteryTemp(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    playkey = models.CharField(db_column='playKey', max_length=10, blank=True, null=True)  # Field name made lowercase.
    serialid = models.CharField(db_column='SerialID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    serialdate = models.CharField(db_column='SerialDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(max_length=16, blank=True, null=True)
    number = models.CharField(db_column='Number', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lottime = models.DateTimeField(db_column='LotTime', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(blank=True, null=True)
    gamename = models.CharField(db_column='GameName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game_lottery_temp'


class GameSet(models.Model):
    playkey = models.CharField(db_column='playKey', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ckey = models.CharField(max_length=60, blank=True, null=True)
    choose = models.IntegerField()
    title = models.CharField(max_length=120, blank=True, null=True)
    mintimes = models.DecimalField(db_column='Mintimes', max_digits=4, decimal_places=2)  # Field name made lowercase.
    times_1700 = models.IntegerField(db_column='Times_1700', blank=True, null=True)  # Field name made lowercase.
    times_a = models.IntegerField(db_column='Times_A')  # Field name made lowercase.
    times_b = models.IntegerField(db_column='Times_B')  # Field name made lowercase.
    times_c = models.IntegerField(db_column='Times_C')  # Field name made lowercase.
    times_d = models.IntegerField(db_column='Times_D')  # Field name made lowercase.
    prize_1700 = models.CharField(db_column='Prize_1700', max_length=80, blank=True, null=True)  # Field name made lowercase.
    prize_a = models.CharField(db_column='Prize_A', max_length=80)  # Field name made lowercase.
    prize_b = models.CharField(db_column='Prize_B', max_length=80)  # Field name made lowercase.
    prize_c = models.CharField(db_column='Prize_C', max_length=80)  # Field name made lowercase.
    prize_d = models.CharField(db_column='Prize_D', max_length=80)  # Field name made lowercase.
    per_1700 = models.IntegerField(db_column='Per_1700')  # Field name made lowercase.
    per_a = models.IntegerField(db_column='Per_A')  # Field name made lowercase.
    per_b = models.IntegerField(db_column='Per_B')  # Field name made lowercase.
    per_c = models.IntegerField(db_column='Per_C')  # Field name made lowercase.
    per_d = models.IntegerField(db_column='Per_D')  # Field name made lowercase.
    pernums_1700 = models.IntegerField(db_column='Pernums_1700')  # Field name made lowercase.
    pernums_a = models.IntegerField(db_column='Pernums_A')  # Field name made lowercase.
    pernums_b = models.IntegerField(db_column='Pernums_B')  # Field name made lowercase.
    pernums_c = models.IntegerField(db_column='Pernums_C')  # Field name made lowercase.
    pernums_d = models.IntegerField(db_column='Pernums_D')  # Field name made lowercase.
    perall_1700 = models.FloatField(db_column='Perall_1700')  # Field name made lowercase.
    perall_a = models.FloatField(db_column='Perall_A')  # Field name made lowercase.
    perall_b = models.FloatField(db_column='Perall_B')  # Field name made lowercase.
    perall_c = models.FloatField(db_column='Perall_C')  # Field name made lowercase.
    perall_d = models.FloatField(db_column='Perall_D')  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_set'


class GameSscList(models.Model):
    fullname = models.CharField(max_length=60, blank=True, null=True)
    ckey = models.CharField(max_length=30, blank=True, null=True)
    skey = models.CharField(max_length=60, blank=True, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)
    cate = models.CharField(max_length=30, blank=True, null=True)
    content = models.CharField(max_length=300, blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    shownum = models.IntegerField(blank=True, null=True)
    minnum = models.IntegerField(blank=True, null=True)
    maxnum = models.IntegerField(blank=True, null=True)
    show_key = models.CharField(max_length=600, blank=True, null=True)
    show_other = models.CharField(max_length=600, blank=True, null=True)
    max_select = models.IntegerField(blank=True, null=True)
    min_select = models.IntegerField(blank=True, null=True)
    is_yes = models.CharField(max_length=6, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ball_type = models.CharField(max_length=20, blank=True, null=True)
    fullname_tw = models.CharField(max_length=60, blank=True, null=True)
    code_tw = models.CharField(max_length=30, blank=True, null=True)
    cate_tw = models.CharField(max_length=30, blank=True, null=True)
    content_tw = models.CharField(max_length=300, blank=True, null=True)
    example_tw = models.TextField(blank=True, null=True)
    help_tw = models.TextField(blank=True, null=True)
    title_tw = models.CharField(max_length=150, blank=True, null=True)
    show_key_tw = models.CharField(max_length=600, blank=True, null=True)
    show_other_tw = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_ssc_list'


class GameSscSet(models.Model):
    list_id = models.CharField(unique=True, max_length=20)
    maxdouble = models.IntegerField()
    fs = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_ssc_set'


class GameTime(models.Model):
    playkey = models.CharField(db_column='playKey', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lotnum = models.CharField(db_column='lotNum', max_length=6, blank=True, null=True)  # Field name made lowercase.
    begintime = models.TimeField(db_column='beginTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    lottime = models.TimeField(db_column='lotTime', blank=True, null=True)  # Field name made lowercase.
    useweek = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_time'


class GameType(models.Model):
    fullname = models.CharField(max_length=90, blank=True, null=True)
    fullname_tw = models.CharField(max_length=90, blank=True, null=True)
    ckey = models.CharField(max_length=30, blank=True, null=True)
    cate = models.CharField(max_length=30, blank=True, null=True)
    skey = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=300, blank=True, null=True)
    codea = models.CharField(db_column='codeA', max_length=300, blank=True, null=True)  # Field name made lowercase.
    codeb = models.CharField(db_column='codeB', max_length=300, blank=True, null=True)  # Field name made lowercase.
    codec = models.CharField(db_column='codeC', max_length=300, blank=True, null=True)  # Field name made lowercase.
    coded = models.CharField(db_column='codeD', max_length=300, blank=True, null=True)  # Field name made lowercase.
    firstcode = models.CharField(max_length=16, blank=True, null=True)
    orders = models.CharField(max_length=10, blank=True, null=True)
    qishu = models.CharField(max_length=4, blank=True, null=True)
    lot_date = models.CharField(max_length=30, blank=True, null=True)
    lot_num = models.CharField(max_length=16, blank=True, null=True)
    lot_begin = models.CharField(max_length=10, blank=True, null=True)
    lot_end = models.CharField(max_length=10, blank=True, null=True)
    type_group = models.CharField(max_length=10, blank=True, null=True)
    list_group = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField()
    statusa = models.IntegerField(db_column='statusA')  # Field name made lowercase.
    statusb = models.IntegerField(db_column='statusB')  # Field name made lowercase.
    statusc = models.IntegerField(db_column='statusC')  # Field name made lowercase.
    statusd = models.IntegerField(db_column='statusD')  # Field name made lowercase.
    testline = models.IntegerField()
    bet = models.IntegerField()
    versions = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    procode = models.CharField(max_length=300, blank=True, null=True)
    useweek = models.CharField(max_length=20)
    showstatus = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'game_type'


class GameTypeAg(models.Model):
    prefix = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.IntegerField()
    higher_id = models.IntegerField()
    proxy = models.IntegerField()
    playkey = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField()
    update_user = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_type_ag'


class GameVirprizeRank(models.Model):
    username = models.CharField(max_length=40)
    fullname = models.CharField(max_length=40)
    pri_money = models.CharField(max_length=10)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_virprize_rank'


class LiveGiftlist(models.Model):
    dept_id = models.CharField(max_length=10)
    buyid = models.CharField(max_length=30, blank=True, null=True)
    playkey = models.CharField(max_length=20)
    list_id = models.CharField(max_length=30)
    user_id = models.IntegerField()
    up6_id = models.IntegerField()
    up5_id = models.IntegerField()
    up4_id = models.IntegerField()
    up3_id = models.IntegerField()
    up2_id = models.IntegerField()
    up1_id = models.IntegerField()
    up0_id = models.IntegerField()
    camgirl_id = models.IntegerField()
    money = models.CharField(max_length=20)
    afterpoints = models.DecimalField(max_digits=15, decimal_places=6)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_giftlist'


class LiveSchedule(models.Model):
    date = models.DateField()
    playkey = models.CharField(max_length=20)
    camgirl_id = models.IntegerField()
    hours = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_schedule'


class Log(models.Model):
    mode = models.PositiveIntegerField()
    type = models.CharField(max_length=30)
    text = models.TextField()
    user = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log'


class PoolLog(models.Model):
    period = models.CharField(primary_key=True, max_length=30)
    income = models.FloatField()
    pay = models.FloatField()
    profit = models.FloatField()
    money = models.FloatField()
    proc = models.FloatField()
    status = models.SmallIntegerField()
    playkey = models.CharField(db_column='playKey', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pool_log'
        unique_together = (('period', 'playkey'),)


class PoolSetting(models.Model):
    proctype = models.CharField(primary_key=True, max_length=10)
    money = models.FloatField()
    playkey = models.CharField(db_column='playKey', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pool_setting'
        unique_together = (('proctype', 'playkey'),)


class PrizeTop(models.Model):
    status = models.IntegerField(blank=True, null=True)
    top_max_num = models.IntegerField(blank=True, null=True)
    top_max_money = models.CharField(max_length=8, blank=True, null=True)
    top_limit_time = models.IntegerField(blank=True, null=True)
    is_open_virtual = models.IntegerField(blank=True, null=True)
    top_vir_min = models.CharField(max_length=8, blank=True, null=True)
    top_vir_max = models.CharField(max_length=8, blank=True, null=True)
    top_vir_game = models.CharField(max_length=100, blank=True, null=True)
    top_vir_nick = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prize_top'


class SchedLongcount(models.Model):
    date = models.DateField()
    playkey = models.CharField(max_length=10)
    list = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sched_longcount'
        unique_together = (('date', 'playkey'),)


class Super(models.Model):
    total = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'super'


class SuperLog(models.Model):
    user_id = models.IntegerField()
    content = models.CharField(max_length=2000)
    beforetotal = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    income = models.DecimalField(max_digits=20, decimal_places=2)
    outlay = models.DecimalField(max_digits=20, decimal_places=2)
    aftertotal = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()
    super_status = models.SmallIntegerField(blank=True, null=True)
    super_betmin = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'super_log'


class SuperSet(models.Model):
    bet = models.IntegerField(unique=True)
    perent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'super_set'


class SuperUser(models.Model):
    user_id = models.IntegerField()
    total = models.DecimalField(max_digits=20, decimal_places=2)
    betmin = models.IntegerField()
    num = models.IntegerField()
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'super_user'


class System(models.Model):
    mingetcash_amount = models.IntegerField(db_column='MinGetCash_amount', blank=True, null=True)  # Field name made lowercase.
    maxgetcash_num = models.IntegerField(db_column='MaxGetCash_num', blank=True, null=True)  # Field name made lowercase.
    modes_putcash = models.IntegerField(db_column='modes_PutCash', blank=True, null=True)  # Field name made lowercase.
    modes_gifts = models.IntegerField(blank=True, null=True)
    modes_gifts_money = models.CharField(max_length=20, blank=True, null=True)
    minputcash_amount = models.CharField(db_column='MinPutCash_amount', max_length=30, blank=True, null=True)  # Field name made lowercase.
    minputcash_ren = models.CharField(db_column='MinPutCash_ren', max_length=30, blank=True, null=True)  # Field name made lowercase.
    getfee_single = models.CharField(db_column='GetFee_Single', max_length=48, blank=True, null=True)  # Field name made lowercase.
    getfee_single_rate = models.CharField(db_column='GetFee_Single_Rate', max_length=18, blank=True, null=True)  # Field name made lowercase.
    modes_rebate = models.CharField(db_column='Modes_Rebate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mention = models.CharField(max_length=30, blank=True, null=True)
    maxbonus = models.CharField(db_column='MaxBonus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    minbonus = models.CharField(db_column='MinBonus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    limit_betting = models.CharField(db_column='Limit_Betting', max_length=8, blank=True, null=True)  # Field name made lowercase.
    auto_jies_begin = models.CharField(db_column='Auto_JieS_Begin', max_length=30, blank=True, null=True)  # Field name made lowercase.
    auto_jies_end = models.CharField(db_column='Auto_JieS_End', max_length=30, blank=True, null=True)  # Field name made lowercase.
    del_member_date = models.IntegerField(db_column='Del_Member_date', blank=True, null=True)  # Field name made lowercase.
    modes = models.CharField(db_column='Modes', max_length=90, blank=True, null=True)  # Field name made lowercase.
    remodes = models.CharField(db_column='Remodes', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fixedmodes = models.CharField(db_column='FixedModes', max_length=5, blank=True, null=True)  # Field name made lowercase.
    automodes = models.CharField(db_column='AutoModes', max_length=5, blank=True, null=True)  # Field name made lowercase.
    maxbank = models.CharField(db_column='MaxBank', max_length=2, blank=True, null=True)  # Field name made lowercase.
    minmodejiao = models.CharField(db_column='MinModeJiao', max_length=5, blank=True, null=True)  # Field name made lowercase.
    minmodefen = models.CharField(db_column='MinModeFen', max_length=5, blank=True, null=True)  # Field name made lowercase.
    isangle = models.CharField(db_column='IsAngle', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ispoint = models.CharField(db_column='IsPoint', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ischase = models.CharField(db_column='IsChase', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ischargeforhig = models.CharField(db_column='IsChargeForHig', max_length=5, blank=True, null=True)  # Field name made lowercase.
    issendmsg = models.CharField(db_column='IsSendMsg', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ispritop = models.CharField(db_column='IsPriTop', max_length=5, blank=True, null=True)  # Field name made lowercase.
    maxprobonus = models.CharField(db_column='MaxProBonus', max_length=5, blank=True, null=True)  # Field name made lowercase.
    recommend = models.CharField(db_column='Recommend', max_length=10, blank=True, null=True)  # Field name made lowercase.
    serviceurl = models.CharField(db_column='ServiceUrl', max_length=120, blank=True, null=True)  # Field name made lowercase.
    accquo = models.CharField(db_column='AccQuo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    onlines = models.CharField(db_column='OnLines', max_length=4, blank=True, null=True)  # Field name made lowercase.
    basicmodes = models.CharField(db_column='basicModes', max_length=5)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'system'


class Text(models.Model):
    type = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'text'


class UserBank(models.Model):
    userid = models.IntegerField()
    password = models.CharField(max_length=40)
    bankname = models.CharField(max_length=30, blank=True, null=True)
    banknum = models.CharField(max_length=30, blank=True, null=True)
    get_amount_num = models.IntegerField(blank=True, null=True)
    get_amount_date = models.DateField(blank=True, null=True)
    golds = models.CharField(max_length=20, blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)
    hig_amount = models.CharField(max_length=20, blank=True, null=True)
    low_amount = models.CharField(max_length=20, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_bank'


class UserBankLog(models.Model):
    userid = models.IntegerField()
    accountid = models.CharField(max_length=30, blank=True, null=True)
    floatid = models.CharField(max_length=60, blank=True, null=True)
    errorcode = models.IntegerField(db_column='ErrorCode')  # Field name made lowercase.
    errormsg = models.CharField(db_column='ErrorMsg', max_length=250)  # Field name made lowercase.
    errorcodep = models.IntegerField(db_column='ErrorCodeP')  # Field name made lowercase.
    errormsgp = models.TextField(db_column='ErrorMsgP')  # Field name made lowercase.
    cate = models.CharField(max_length=26, blank=True, null=True)
    moneys = models.CharField(max_length=16, blank=True, null=True)
    amount = models.CharField(max_length=30, blank=True, null=True)
    hig_amount = models.CharField(max_length=30, blank=True, null=True)
    low_amount = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=300, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    playkey = models.CharField(max_length=20, blank=True, null=True)
    modes = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_bank_log'


class UserRebate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.PositiveIntegerField()
    playkey = models.CharField(db_column='PlayKey', max_length=30, blank=True, null=True)  # Field name made lowercase.
    itemkey = models.CharField(db_column='ItemKey', max_length=6, blank=True, null=True)  # Field name made lowercase.
    modes = models.BigIntegerField(db_column='Modes')  # Field name made lowercase.
    number = models.FloatField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'user_rebate'
