# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Active(models.Model):
    activeid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    typeid0 = models.IntegerField()
    typeid1 = models.IntegerField()
    typeid2 = models.IntegerField()
    typeid3 = models.IntegerField()
    typeid4 = models.IntegerField()
    typeid5 = models.IntegerField()
    typeid6 = models.IntegerField()
    typeid7 = models.IntegerField()
    typeid8 = models.IntegerField()
    typeid9 = models.IntegerField()
    people_limit = models.IntegerField()
    reset = models.IntegerField()
    levelup = models.IntegerField()
    status = models.IntegerField()
    showtime = models.DateTimeField()
    noshowtime = models.DateTimeField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active'


class ActiveLog(models.Model):
    user_id = models.IntegerField()
    activeid = models.IntegerField()
    reset = models.IntegerField()
    levelup = models.IntegerField()
    unit = models.IntegerField()
    amount = models.FloatField()
    note = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_log'


class ActiveRule(models.Model):
    typeid = models.AutoField(primary_key=True)
    typename = models.CharField(max_length=20)
    sclass0 = models.IntegerField()
    sclass1 = models.IntegerField()
    sclass2 = models.IntegerField()
    enough0 = models.FloatField()
    enough1 = models.FloatField()
    enough2 = models.FloatField()
    reset = models.IntegerField()
    levelup = models.IntegerField()
    giveclass = models.IntegerField()
    unit = models.IntegerField()
    amount0 = models.FloatField()
    amount1 = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active_rule'


class ActiveTimes(models.Model):
    user_id = models.IntegerField()
    dates = models.DateField()
    pay = models.IntegerField()
    bet = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_times'


class ActiveUser(models.Model):
    user_id = models.IntegerField()
    activeid = models.IntegerField()
    times = models.IntegerField()
    standard = models.CharField(max_length=20)
    give = models.CharField(max_length=20)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_user'


class Activity(models.Model):
    type = models.CharField(max_length=1)
    title = models.CharField(max_length=50)
    reward_type = models.CharField(max_length=255)
    activity_reward_id = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    show_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    content = models.TextField(blank=True, null=True)
    show_at_index = models.CharField(max_length=255)
    show_at_bulletin = models.CharField(max_length=255)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity'


class ActivityReward(models.Model):
    cnd = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=1)
    target = models.CharField(max_length=1)
    rewardtype = models.IntegerField(blank=True, null=True)
    num_01 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_02 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_03 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_04 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_05 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_06 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_07 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_08 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_09 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_10 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_11 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_12 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_13 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_14 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_15 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_16 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_17 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_18 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_19 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    num_20 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_01 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_02 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_03 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_04 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_05 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_06 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_07 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_08 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_09 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_10 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_11 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_12 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_13 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_14 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_15 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_16 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_17 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_18 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_19 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rewardnum_20 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_reward'


class ActivityRewardCnd(models.Model):
    type = models.CharField(max_length=1)
    fullname = models.CharField(max_length=50)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_reward_cnd'


class ActivityRewardLog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_ip = models.CharField(max_length=50, blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    reward_id = models.IntegerField(blank=True, null=True)
    num_before = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    num_def = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    num_after = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reward_give = models.CharField(max_length=1)
    reward_type = models.CharField(max_length=1, blank=True, null=True)
    reward_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reward_prize = models.CharField(max_length=1)
    reward_target = models.CharField(max_length=1)
    auto_prize = models.CharField(max_length=1)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_reward_log'


class ActivityRewardRnd(models.Model):
    rand_num = models.IntegerField(blank=True, null=True)
    rand_01 = models.IntegerField(blank=True, null=True)
    rand_02 = models.IntegerField(blank=True, null=True)
    rand_03 = models.IntegerField(blank=True, null=True)
    rand_04 = models.IntegerField(blank=True, null=True)
    rand_05 = models.IntegerField(blank=True, null=True)
    rand_06 = models.IntegerField(blank=True, null=True)
    rand_07 = models.IntegerField(blank=True, null=True)
    rand_08 = models.IntegerField(blank=True, null=True)
    rand_09 = models.IntegerField(blank=True, null=True)
    rand_10 = models.IntegerField(blank=True, null=True)
    rand_11 = models.IntegerField(blank=True, null=True)
    rand_12 = models.IntegerField(blank=True, null=True)
    rand_13 = models.IntegerField(blank=True, null=True)
    rand_14 = models.IntegerField(blank=True, null=True)
    rand_15 = models.IntegerField(blank=True, null=True)
    rand_16 = models.IntegerField(blank=True, null=True)
    rand_17 = models.IntegerField(blank=True, null=True)
    rand_18 = models.IntegerField(blank=True, null=True)
    rand_19 = models.IntegerField(blank=True, null=True)
    rand_20 = models.IntegerField(blank=True, null=True)
    rand_21 = models.IntegerField(blank=True, null=True)
    rand_22 = models.IntegerField(blank=True, null=True)
    rand_23 = models.IntegerField(blank=True, null=True)
    rand_24 = models.IntegerField(blank=True, null=True)
    rand_25 = models.IntegerField(blank=True, null=True)
    rtype_01 = models.CharField(max_length=1)
    rtype_02 = models.CharField(max_length=1)
    rtype_03 = models.CharField(max_length=1)
    rtype_04 = models.CharField(max_length=1)
    rtype_05 = models.CharField(max_length=1)
    rtype_06 = models.CharField(max_length=1)
    rtype_07 = models.CharField(max_length=1)
    rtype_08 = models.CharField(max_length=1)
    rtype_09 = models.CharField(max_length=1)
    rtype_10 = models.CharField(max_length=1)
    rtype_11 = models.CharField(max_length=1)
    rtype_12 = models.CharField(max_length=1)
    rtype_13 = models.CharField(max_length=1)
    rtype_14 = models.CharField(max_length=1)
    rtype_15 = models.CharField(max_length=1)
    rtype_16 = models.CharField(max_length=1)
    rtype_17 = models.CharField(max_length=1)
    rtype_18 = models.CharField(max_length=1)
    rtype_19 = models.CharField(max_length=1)
    rtype_20 = models.CharField(max_length=1)
    rtype_21 = models.CharField(max_length=1)
    rtype_22 = models.CharField(max_length=1)
    rtype_23 = models.CharField(max_length=1)
    rtype_24 = models.CharField(max_length=1)
    rtype_25 = models.CharField(max_length=1)
    rnum_01 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_02 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_03 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_04 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_05 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_06 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_07 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_08 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_09 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_10 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_11 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_12 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_13 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_14 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_15 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_16 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_17 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_18 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_19 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_20 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_21 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_22 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_23 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_24 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnum_25 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_reward_rnd'


class AdminSystem(models.Model):
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=45, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_system'


class BankBack(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    back_money2 = models.CharField(max_length=20, blank=True, null=True)
    b_befor = models.CharField(max_length=20, blank=True, null=True)
    b_after = models.CharField(max_length=20, blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    lotteryid = models.IntegerField(blank=True, null=True)
    follows = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_back'


class Banner(models.Model):
    banner_type_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField()
    staytime = models.SmallIntegerField(blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    href = models.CharField(max_length=120, blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'banner'


class BannerType(models.Model):
    area = models.CharField(max_length=120, blank=True, null=True)
    picwidth = models.SmallIntegerField(blank=True, null=True)
    picheight = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'banner_type'


class BetResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    game_kinds_id = models.IntegerField()
    game_kinds_skey = models.CharField(max_length=50)
    bet_id = models.CharField(max_length=100, blank=True, null=True)
    bet_gameid = models.CharField(max_length=100, blank=True, null=True)
    bet_gamename = models.CharField(max_length=100, blank=True, null=True)
    bet_round = models.CharField(max_length=20, blank=True, null=True)
    bet_userid = models.CharField(max_length=20, blank=True, null=True)
    bet_username = models.CharField(max_length=20, blank=True, null=True)
    trans_id = models.CharField(max_length=100, blank=True, null=True)
    bet = models.CharField(max_length=20)
    bet_available = models.CharField(max_length=20)
    prize = models.CharField(max_length=20)
    winlose = models.CharField(max_length=20)
    jcon = models.CharField(max_length=20, blank=True, null=True)
    jwin = models.CharField(max_length=20, blank=True, null=True)
    selfpoint = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    bet_time = models.DateTimeField(blank=True, null=True)
    prize_time = models.DateTimeField(blank=True, null=True)
    platform = models.CharField(max_length=10, blank=True, null=True)
    beforepoints = models.FloatField(db_column='beforePoints', blank=True, null=True)  # Field name made lowercase.
    afterpoints = models.FloatField(db_column='afterPoints', blank=True, null=True)  # Field name made lowercase.
    experience = models.CharField(max_length=1)
    status = models.IntegerField()
    log = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bet_result'


class BlockString(models.Model):
    string = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_string'


class Bulletin(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1)
    status_back = models.CharField(max_length=1)
    loginboard = models.CharField(max_length=45)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin'


class ContactTalk(models.Model):
    user_id_a = models.IntegerField()
    user_id_b = models.IntegerField()
    talk_idx = models.IntegerField()
    content = models.CharField(max_length=200)
    readcon = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contact_talk'


class CoopList(models.Model):
    prefix = models.CharField(max_length=10, blank=True, null=True)
    prefix_name = models.CharField(max_length=45)
    topuser = models.CharField(max_length=45)
    downuser = models.CharField(max_length=45)
    isproxy = models.IntegerField()
    md5key = models.CharField(max_length=20)
    white_ip = models.TextField()
    lotto = models.IntegerField(db_column='Lotto')  # Field name made lowercase.
    live = models.IntegerField(db_column='Live')  # Field name made lowercase.
    sport = models.CharField(db_column='Sport', max_length=45)  # Field name made lowercase.
    agurl1 = models.CharField(max_length=100, blank=True, null=True)
    agurl2 = models.CharField(max_length=100, blank=True, null=True)
    site_id = models.CharField(max_length=10, blank=True, null=True)
    handicaps = models.CharField(max_length=2, blank=True, null=True)
    chat = models.IntegerField()
    gift = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coop_list'


class GameKinds(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    skey = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game_kinds'


class IpAllowList(models.Model):
    isproxy = models.CharField(max_length=10, blank=True, null=True)
    ipaddress = models.CharField(max_length=50)
    enabled = models.CharField(max_length=1)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ip_allow_list'
        unique_together = (('ipaddress', 'enabled'),)


class IpBlockList(models.Model):
    type = models.CharField(max_length=5)
    condition = models.CharField(max_length=50)
    enabled = models.CharField(max_length=1)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ip_block_list'


class ListBank(models.Model):
    bank = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'list_bank'


class ListCity(models.Model):
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'list_city'


class LiveCamgirl(models.Model):
    id = models.IntegerField(primary_key=True)
    dept_id = models.CharField(max_length=10)
    girlname = models.CharField(max_length=20)
    girlname_tw = models.CharField(max_length=45)
    height = models.IntegerField()
    weight = models.IntegerField()
    year = models.DateField()
    bwh = models.CharField(max_length=20)
    icon = models.TextField()
    note = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_camgirl'


class LiveDept(models.Model):
    deptid = models.CharField(max_length=45)
    deptname = models.CharField(max_length=20)
    username = models.CharField(max_length=255)
    playkey = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_dept'


class LiveGiftitem(models.Model):
    list_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    name_tw = models.CharField(max_length=20)
    money = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_giftitem'


class LiveMarquee(models.Model):
    playkey = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    minute = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_marquee'


class LiveStream(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=45)
    blade = models.CharField(max_length=20, blank=True, null=True)
    pc = models.IntegerField(blank=True, null=True)
    mac = models.IntegerField(blank=True, null=True)
    app = models.IntegerField(blank=True, null=True)
    deptarr = models.CharField(max_length=40)
    sorts = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_stream'


class MenuSystem(models.Model):
    bo = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField()
    cid = models.IntegerField()
    cname = models.CharField(max_length=20)
    path = models.CharField(max_length=100)
    auth = models.CharField(max_length=50)
    state = models.IntegerField()
    target = models.IntegerField()
    icon = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'menu_system'


class MessageCanned(models.Model):
    message = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'message_canned'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class OperationType(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'operation_type'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'password_resets'


class Payrecord(models.Model):
    payid = models.AutoField(db_column='payID', primary_key=True)  # Field name made lowercase.
    paynumid = models.CharField(db_column='payNumID', unique=True, max_length=50)  # Field name made lowercase.
    paytype = models.CharField(db_column='payType', max_length=50)  # Field name made lowercase.
    payuser = models.CharField(db_column='payUser', max_length=50)  # Field name made lowercase.
    paymoney = models.FloatField(db_column='payMoney')  # Field name made lowercase.
    paystate = models.CharField(db_column='payState', max_length=50)  # Field name made lowercase.
    userrealname = models.CharField(db_column='userRealName', max_length=50)  # Field name made lowercase.
    curmoney = models.FloatField(db_column='curMoney')  # Field name made lowercase.
    oldmoney = models.FloatField(db_column='oldMoney')  # Field name made lowercase.
    thispaystate = models.CharField(db_column='thisPayState', max_length=50)  # Field name made lowercase.
    paytime = models.DateTimeField(db_column='payTime', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=50)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payrecord'


class PointAlter(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'point_alter'


class PointTypes(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'point_types'


class PromoLink(models.Model):
    linkname = models.CharField(max_length=10)
    linkurl = models.CharField(max_length=100)
    userid = models.IntegerField()
    rebate = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    remark = models.CharField(max_length=200)
    times = models.IntegerField()
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promo_link'


class Rebate(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    rebate = models.FloatField()
    quota = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rebate'


class Reception(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    status = models.IntegerField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reception'


class Rotation(models.Model):
    phone = models.SmallIntegerField()
    sort = models.SmallIntegerField()
    enable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rotation'


class ScoreSet(models.Model):
    money = models.IntegerField()
    score = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'score_set'


class SecureQuestion(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'secure_question'


class ServiceTalkd(models.Model):
    user_id = models.IntegerField()
    mid = models.IntegerField()
    talk_idx = models.IntegerField()
    content = models.CharField(max_length=200)
    readcon = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_talkd'


class ServiceTalkm(models.Model):
    user_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    kf_user_id = models.IntegerField(blank=True, null=True)
    sound = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_talkm'


class Session(models.Model):
    user_id = models.IntegerField()
    ip_address = models.CharField(max_length=45)
    user_agent = models.TextField()
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'session'


class Suggest(models.Model):
    user_id = models.IntegerField()
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'suggest'


class SysBank(models.Model):
    bankcode = models.CharField(db_column='bankCode', max_length=10)  # Field name made lowercase.
    bankname = models.CharField(max_length=255, blank=True, null=True)
    banktype = models.CharField(max_length=10, blank=True, null=True)
    bank_branch = models.CharField(max_length=255, blank=True, null=True)
    realname = models.CharField(max_length=255, blank=True, null=True)
    banknum = models.CharField(max_length=255)
    bankemail = models.TextField(db_column='bankEmail', blank=True, null=True)  # Field name made lowercase.
    min = models.IntegerField()
    max = models.IntegerField()
    inouts = models.IntegerField()
    groupid = models.IntegerField(blank=True, null=True)
    enabled = models.CharField(max_length=1)
    enabled_phone = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_bank'


class SysBankGroup(models.Model):
    vip = models.IntegerField()
    groupname = models.CharField(max_length=20)
    note = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_bank_group'


class SysBankList(models.Model):
    code = models.CharField(max_length=10)
    bankname = models.CharField(db_column='bankName', max_length=255)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_bank_list'


class SysCode(models.Model):
    fieldname = models.CharField(max_length=20)
    codeid = models.CharField(max_length=10)
    codename = models.CharField(max_length=20)
    codevalue = models.CharField(max_length=20)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_code'


class SysDividend(models.Model):
    name = models.CharField(max_length=10)
    members = models.SmallIntegerField()
    quantity = models.CharField(max_length=45)
    percent = models.CharField(max_length=45)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_dividend'


class SysFunds(models.Model):
    user_id = models.IntegerField()
    money = models.IntegerField()
    money_r = models.IntegerField()
    cate = models.CharField(max_length=16, blank=True, null=True)
    bankcode = models.CharField(db_column='bankCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(max_length=20, blank=True, null=True)
    banknum = models.CharField(max_length=255, blank=True, null=True)
    bank_branch = models.CharField(max_length=100, blank=True, null=True)
    bankemail = models.CharField(max_length=255, blank=True, null=True)
    realname = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    user_ip = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    sys_bank = models.CharField(max_length=255, blank=True, null=True)
    sys_bankuername = models.CharField(db_column='sys_bankUerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_banknum = models.CharField(db_column='sys_bankNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_fee = models.IntegerField(blank=True, null=True)
    sys_user_id = models.IntegerField(blank=True, null=True)
    sys_operated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    notetime = models.DateTimeField(blank=True, null=True)
    note2 = models.CharField(max_length=255, blank=True, null=True)
    notetime2 = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    need_water = models.FloatField()
    buy_water = models.FloatField()
    can_with = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sys_funds'


class SysFunds3Rd(models.Model):
    fid = models.CharField(max_length=255)
    support = models.CharField(max_length=10)
    yborderid = models.CharField(max_length=50)
    amount = models.IntegerField()
    bank = models.CharField(max_length=30, blank=True, null=True)
    lastno = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    bankdealid = models.CharField(db_column='bankDealId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dealtime = models.CharField(db_column='dealTime', max_length=14, blank=True, null=True)  # Field name made lowercase.
    payamount = models.IntegerField(db_column='payAmount', blank=True, null=True)  # Field name made lowercase.
    fee = models.IntegerField(blank=True, null=True)
    payresult = models.CharField(db_column='payResult', max_length=2, blank=True, null=True)  # Field name made lowercase.
    errcode = models.CharField(db_column='errCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_funds_3rd'


class SysImage(models.Model):
    filename = models.CharField(max_length=255)
    picwidth = models.SmallIntegerField()
    picheight = models.SmallIntegerField()
    note = models.CharField(max_length=255)
    imgtext = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_image'


class SysMachine(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_machine'


class SysSalary(models.Model):
    purchase = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_salary'


class User(models.Model):
    username = models.CharField(unique=True, max_length=255)
    realname = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=120)
    bank_pwd = models.CharField(max_length=120, blank=True, null=True)
    enabled = models.IntegerField()
    enabled_live = models.IntegerField()
    vip_lot = models.IntegerField()
    depositnum = models.IntegerField()
    disabled_reason = models.CharField(max_length=255, blank=True, null=True)
    isproxy = models.IntegerField()
    proxy_id = models.IntegerField(blank=True, null=True)
    proxynum = models.PositiveIntegerField()
    downcounts = models.PositiveIntegerField(db_column='downCounts')  # Field name made lowercase.
    note = models.CharField(max_length=255, blank=True, null=True)
    location = models.IntegerField()
    salary_set = models.CharField(max_length=20)
    salary = models.CharField(max_length=1)
    bet = models.CharField(max_length=1)
    tr_money = models.CharField(max_length=1)
    role = models.PositiveIntegerField(blank=True, null=True)
    sq_id = models.IntegerField(blank=True, null=True)
    sq_answer = models.CharField(max_length=255, blank=True, null=True)
    nowlogintime = models.DateTimeField(db_column='nowLoginTime', blank=True, null=True)  # Field name made lowercase.
    nowloginip = models.CharField(db_column='nowLoginIp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastlogintime = models.DateTimeField(db_column='lastLoginTime', blank=True, null=True)  # Field name made lowercase.
    lastloginip = models.CharField(db_column='lastLoginIp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    camlot_token = models.CharField(max_length=255, blank=True, null=True)
    backend_token = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=1)
    keepalive_time = models.DateTimeField(blank=True, null=True)
    colorflag = models.IntegerField()
    iconflag = models.IntegerField()
    user_url = models.CharField(max_length=20, blank=True, null=True)
    recharge = models.CharField(max_length=1)
    withdrawl = models.CharField(max_length=1)
    verified = models.CharField(max_length=1)
    miss_num = models.IntegerField()
    handicaps = models.CharField(max_length=1)
    currency = models.CharField(max_length=5, blank=True, null=True)
    credit = models.IntegerField()
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    rpoint = models.DecimalField(max_digits=5, decimal_places=2)
    autopoint = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class UserAdminLoginLogs(models.Model):
    user_id = models.IntegerField()
    login_ip = models.CharField(max_length=255)
    login_web = models.CharField(max_length=30)
    agent = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_admin_login_logs'


class UserAdminLogs(models.Model):
    user = models.CharField(max_length=255)
    operation_type_id = models.IntegerField(blank=True, null=True)
    db = models.CharField(max_length=30, blank=True, null=True)
    table = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField()
    note = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_admin_logs'


class UserAdminLogsLive(models.Model):
    user = models.CharField(max_length=255)
    operation_type_id = models.IntegerField(blank=True, null=True)
    db = models.CharField(max_length=30, blank=True, null=True)
    table = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField()
    note = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_admin_logs_live'


class UserBankCard(models.Model):
    user_id = models.IntegerField()
    bankcode = models.CharField(db_column='bankCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='bankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=255, blank=True, null=True)
    bankbranch = models.CharField(db_column='bankBranch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    banknum = models.CharField(db_column='bankNum', max_length=255)  # Field name made lowercase.
    bankemail = models.CharField(db_column='bankEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enabled = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bank_card'


class UserBonusLog(models.Model):
    user_id = models.IntegerField()
    beforepoints = models.CharField(db_column='beforePoints', max_length=20)  # Field name made lowercase.
    income = models.CharField(max_length=20)
    outlay = models.CharField(max_length=20)
    afterpoints = models.CharField(db_column='afterPoints', max_length=20)  # Field name made lowercase.
    from_user_id = models.IntegerField(blank=True, null=True)
    to_user_id = models.IntegerField(blank=True, null=True)
    point_alter_id = models.IntegerField()
    point_type_id = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bonus_log'


class UserCommissionLog(models.Model):
    datestart = models.DateField(db_column='dateStart')  # Field name made lowercase.
    dateend = models.DateField(db_column='dateEnd')  # Field name made lowercase.
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    up_user_id = models.IntegerField(blank=True, null=True)
    up_username = models.CharField(max_length=255, blank=True, null=True)
    topcomm = models.CharField(max_length=20)
    profitnloss = models.CharField(db_column='profitNLoss', max_length=20)  # Field name made lowercase.
    commission = models.CharField(max_length=20)
    commission_real = models.CharField(max_length=20)
    downcomm = models.CharField(max_length=20, blank=True, null=True)
    receive = models.CharField(max_length=1)
    received_at = models.DateTimeField(blank=True, null=True)
    exc_user_id = models.IntegerField(blank=True, null=True)
    dividend = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_commission_log'


class UserDartLog(models.Model):
    user_id = models.IntegerField()
    usefree = models.CharField(max_length=1)
    money = models.SmallIntegerField()
    times = models.SmallIntegerField()
    amount = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_dart_log'


class UserDaymaxLive(models.Model):
    user_id = models.CharField(max_length=45, blank=True, null=True)
    nums = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_daymax_live'


class UserDividend(models.Model):
    user_id = models.IntegerField()
    level = models.IntegerField()
    members = models.SmallIntegerField()
    quantity = models.IntegerField()
    percent = models.SmallIntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_dividend'


class UserDividendt(models.Model):
    user_id = models.IntegerField()
    level = models.IntegerField()
    members = models.SmallIntegerField()
    quantity = models.IntegerField()
    percent = models.SmallIntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_dividendt'


class UserFunds(models.Model):
    user_id = models.IntegerField()
    money = models.IntegerField()
    money_r = models.IntegerField()
    cate = models.CharField(max_length=16, blank=True, null=True)
    bankcode = models.CharField(db_column='bankCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(max_length=20, blank=True, null=True)
    banknum = models.CharField(max_length=255, blank=True, null=True)
    bank_branch = models.CharField(max_length=100, blank=True, null=True)
    bankemail = models.CharField(max_length=255, blank=True, null=True)
    realname = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    user_ip = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    sys_bank = models.CharField(max_length=255, blank=True, null=True)
    sys_bankuername = models.CharField(db_column='sys_bankUerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_banknum = models.CharField(db_column='sys_bankNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_fee = models.IntegerField(blank=True, null=True)
    sys_user_id = models.IntegerField(blank=True, null=True)
    sys_operated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    notetime = models.DateTimeField(blank=True, null=True)
    note2 = models.CharField(max_length=255, blank=True, null=True)
    notetime2 = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    need_water = models.FloatField()
    buy_water = models.FloatField()
    can_with = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user_funds'


class UserFunds3Rd(models.Model):
    fid = models.CharField(max_length=255)
    support = models.CharField(max_length=10)
    yborderid = models.CharField(max_length=50)
    amount = models.IntegerField()
    bank = models.CharField(max_length=30, blank=True, null=True)
    lastno = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    bankdealid = models.CharField(db_column='bankDealId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dealtime = models.CharField(db_column='dealTime', max_length=14, blank=True, null=True)  # Field name made lowercase.
    payamount = models.IntegerField(db_column='payAmount', blank=True, null=True)  # Field name made lowercase.
    fee = models.IntegerField(blank=True, null=True)
    payresult = models.CharField(db_column='payResult', max_length=2, blank=True, null=True)  # Field name made lowercase.
    errcode = models.CharField(db_column='errCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_funds_3rd'


class UserFunds3RdLive(models.Model):
    fid = models.CharField(max_length=255)
    support = models.CharField(max_length=10)
    yborderid = models.CharField(max_length=50)
    amount = models.IntegerField()
    bank = models.CharField(max_length=30, blank=True, null=True)
    lastno = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    bankdealid = models.CharField(db_column='bankDealId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dealtime = models.CharField(db_column='dealTime', max_length=14, blank=True, null=True)  # Field name made lowercase.
    payamount = models.IntegerField(db_column='payAmount', blank=True, null=True)  # Field name made lowercase.
    fee = models.IntegerField(blank=True, null=True)
    payresult = models.CharField(db_column='payResult', max_length=2, blank=True, null=True)  # Field name made lowercase.
    errcode = models.CharField(db_column='errCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_funds_3rd_live'


class UserFundsLive(models.Model):
    user_id = models.IntegerField()
    money = models.IntegerField()
    money_r = models.IntegerField()
    cate = models.CharField(max_length=16, blank=True, null=True)
    bankcode = models.CharField(db_column='bankCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(max_length=20, blank=True, null=True)
    banknum = models.CharField(max_length=255, blank=True, null=True)
    bank_branch = models.CharField(max_length=100, blank=True, null=True)
    bankemail = models.CharField(max_length=255, blank=True, null=True)
    realname = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    user_ip = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    sys_bank = models.CharField(max_length=255, blank=True, null=True)
    sys_bankuername = models.CharField(db_column='sys_bankUerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_banknum = models.CharField(db_column='sys_bankNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_fee = models.IntegerField(blank=True, null=True)
    sys_user_id = models.IntegerField(blank=True, null=True)
    sys_operated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    notetime = models.DateTimeField(blank=True, null=True)
    note2 = models.CharField(max_length=255, blank=True, null=True)
    notetime2 = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    need_water = models.FloatField()
    buy_water = models.FloatField()
    can_with = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user_funds_live'


class UserGiftLive(models.Model):
    dept_id = models.CharField(max_length=10)
    date = models.DateField()
    playkey = models.CharField(max_length=20)
    tablenum = models.CharField(max_length=20)
    list_id = models.CharField(max_length=20)
    dealer_id = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=45)
    count = models.IntegerField()
    money = models.DecimalField(max_digits=20, decimal_places=6)
    up6_id = models.IntegerField()
    up5_id = models.IntegerField()
    up4_id = models.IntegerField()
    up3_id = models.IntegerField()
    up2_id = models.IntegerField()
    up1_id = models.IntegerField()
    up0_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_gift_live'


class UserGiftLot(models.Model):
    dept_id = models.CharField(max_length=10)
    date = models.DateField()
    playkey = models.CharField(max_length=20)
    list_id = models.CharField(max_length=20)
    camgirl_id = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=45)
    count = models.IntegerField()
    money = models.DecimalField(max_digits=20, decimal_places=6)
    up6_id = models.IntegerField()
    up5_id = models.IntegerField()
    up4_id = models.IntegerField()
    up3_id = models.IntegerField()
    up2_id = models.IntegerField()
    up1_id = models.IntegerField()
    up0_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_gift_lot'


class UserLevel(models.Model):
    user_id = models.IntegerField(unique=True)
    higher_id = models.IntegerField(blank=True, null=True)
    vip_id = models.IntegerField()
    levelname = models.CharField(max_length=20)
    vip_exp = models.DecimalField(max_digits=10, decimal_places=2)
    versions = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_level'


class UserLocationLog(models.Model):
    user_id = models.IntegerField()
    location = models.IntegerField()
    beforepoints = models.TextField(db_column='beforePoints', blank=True, null=True)  # Field name made lowercase.
    afterpoints = models.TextField(db_column='afterPoints', blank=True, null=True)  # Field name made lowercase.
    point_alter_id = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_location_log'


class UserLoginLogs(models.Model):
    user_id = models.IntegerField()
    login_ip = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_login_logs'


class UserMapping(models.Model):
    user_id = models.PositiveIntegerField()
    user_pwd = models.CharField(max_length=120, blank=True, null=True)
    game_kinds_id = models.PositiveIntegerField()
    playtimes = models.IntegerField()
    last_login_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_mapping'


class UserMsg(models.Model):
    user_id = models.IntegerField()
    sender_id = models.IntegerField(blank=True, null=True)
    reply_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    beenread = models.CharField(db_column='beenRead', max_length=1)  # Field name made lowercase.
    senderdelete = models.CharField(db_column='senderDelete', max_length=1)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_msg'


class UserOperationLog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    exe_user_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    before_status = models.CharField(max_length=10, blank=True, null=True)
    after_status = models.CharField(max_length=10, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_log'


class UserOperationLogLive(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    exe_user_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    before_status = models.CharField(max_length=10, blank=True, null=True)
    after_status = models.CharField(max_length=10, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_log_live'


class UserPoints(models.Model):
    user_id = models.IntegerField()
    point_types_id = models.IntegerField()
    points = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_points'


class UserPointsDay(models.Model):
    date = models.DateField()
    user_id = models.IntegerField()
    point_types_id = models.IntegerField()
    points = models.FloatField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_points_day'
        unique_together = (('date', 'user_id', 'point_types_id'),)


class UserPointsLog(models.Model):
    user_id = models.IntegerField()
    beforepoints = models.FloatField(db_column='beforePoints')  # Field name made lowercase.
    income = models.FloatField()
    outlay = models.FloatField()
    afterpoints = models.FloatField(db_column='afterPoints')  # Field name made lowercase.
    from_user_id = models.IntegerField(blank=True, null=True)
    to_user_id = models.IntegerField(blank=True, null=True)
    point_alter_id = models.IntegerField()
    point_type_id = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_points_log'


class UserPointsLogLive(models.Model):
    user_id = models.IntegerField()
    beforepoints = models.FloatField(db_column='beforePoints')  # Field name made lowercase.
    income = models.FloatField()
    outlay = models.FloatField()
    afterpoints = models.FloatField(db_column='afterPoints')  # Field name made lowercase.
    from_user_id = models.IntegerField(blank=True, null=True)
    to_user_id = models.IntegerField(blank=True, null=True)
    point_alter_id = models.IntegerField()
    point_type_id = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_points_log_live'


class UserProxy(models.Model):
    proxyid = models.IntegerField(primary_key=True)
    proxyname = models.CharField(max_length=12)
    proxy_rate = models.IntegerField()
    opennum = models.IntegerField()
    proxy_login = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_proxy'


class UserQuotas(models.Model):
    user_id = models.PositiveIntegerField()
    rebate_id = models.PositiveIntegerField()
    quota = models.IntegerField()
    quota_space = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_quotas'


class UserQuotasLog(models.Model):
    user_quotas_id = models.PositiveIntegerField()
    after_quota_space = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    quota_space = models.PositiveIntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_quotas_log'


class UserRates(models.Model):
    game_kind_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    rate = models.FloatField()
    type = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_rates'


class UserRatesLog(models.Model):
    user_rates_id = models.PositiveIntegerField()
    rate = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_rates_log'


class UserRatest(models.Model):
    game_kind_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    rate = models.FloatField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_ratest'


class UserReport(models.Model):
    date = models.DateField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    up_user_id = models.IntegerField(blank=True, null=True)
    up_username = models.CharField(max_length=255, blank=True, null=True)
    game_kinds_id = models.IntegerField()
    game_kinds_skey = models.CharField(max_length=50)
    income = models.CharField(max_length=20)
    outgo = models.CharField(max_length=20)
    bet = models.CharField(max_length=20)
    bet_nc = models.CharField(max_length=20)
    winlose = models.CharField(max_length=20)
    prize = models.CharField(max_length=20)
    real_winlose = models.CharField(max_length=20)
    activity_reward = models.CharField(max_length=20)
    returnpoint = models.CharField(db_column='returnPoint', max_length=20)  # Field name made lowercase.
    salary = models.CharField(max_length=20)
    salary_sin = models.CharField(max_length=20)
    profitnloss = models.CharField(db_column='profitNLoss', max_length=20)  # Field name made lowercase.
    commission = models.CharField(max_length=20)
    dividendrate = models.CharField(db_column='dividendRate', max_length=5)  # Field name made lowercase.
    count = models.IntegerField()
    win = models.IntegerField()
    platform = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_report'


class UserReportRangeSsc(models.Model):
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    up_user_id = models.IntegerField(blank=True, null=True)
    up_username = models.CharField(max_length=255, blank=True, null=True)
    income = models.CharField(max_length=20)
    outgo = models.CharField(max_length=20)
    bet = models.CharField(max_length=20)
    winlose = models.CharField(max_length=20)
    prize = models.CharField(max_length=20)
    real_winlose = models.CharField(max_length=20)
    activity_reward = models.CharField(max_length=20)
    returnpoint = models.CharField(db_column='returnPoint', max_length=20)  # Field name made lowercase.
    salary = models.CharField(max_length=20)
    profitnloss = models.CharField(db_column='profitNLoss', max_length=20)  # Field name made lowercase.
    commission = models.CharField(max_length=20)
    dividendrate = models.CharField(db_column='dividendRate', max_length=5)  # Field name made lowercase.
    count = models.IntegerField()
    win = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_report_range_ssc'


class UserReportSsc(models.Model):
    date = models.DateField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    up_user_id = models.IntegerField(blank=True, null=True)
    up_username = models.CharField(max_length=255, blank=True, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=6)
    outgo = models.DecimalField(max_digits=10, decimal_places=6)
    bet = models.DecimalField(max_digits=10, decimal_places=6)
    betok = models.DecimalField(max_digits=10, decimal_places=6)
    wait = models.DecimalField(max_digits=10, decimal_places=6)
    winlose = models.DecimalField(max_digits=10, decimal_places=6)
    prize = models.DecimalField(max_digits=10, decimal_places=6)
    real_winlose = models.DecimalField(max_digits=10, decimal_places=6)
    activity_reward = models.DecimalField(max_digits=10, decimal_places=6)
    returnpoint = models.DecimalField(db_column='returnPoint', max_digits=10, decimal_places=6)  # Field name made lowercase.
    salary = models.DecimalField(max_digits=10, decimal_places=6)
    salary_sin = models.DecimalField(max_digits=10, decimal_places=6)
    profitnloss = models.DecimalField(db_column='profitNLoss', max_digits=10, decimal_places=6)  # Field name made lowercase.
    commission = models.DecimalField(max_digits=10, decimal_places=6)
    dividendrate = models.CharField(db_column='dividendRate', max_length=5)  # Field name made lowercase.
    count = models.IntegerField()
    win = models.IntegerField()
    pay = models.IntegerField()
    pay_total = models.DecimalField(max_digits=10, decimal_places=6)
    withdrawal = models.IntegerField()
    withdrawal_total = models.DecimalField(max_digits=10, decimal_places=6)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_report_ssc'


class UserSalaryLog(models.Model):
    date = models.DateField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    up_user_id = models.IntegerField(blank=True, null=True)
    up_username = models.CharField(max_length=255, blank=True, null=True)
    bet = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    receive = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_salary_log'


class UserVerifyProxy(models.Model):
    from_id = models.IntegerField()
    from_username = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    qq = models.CharField(max_length=40)
    wechat = models.CharField(max_length=40)
    sq_id = models.IntegerField()
    sq_answer = models.CharField(max_length=60)
    user_url = models.CharField(max_length=20)
    area = models.CharField(max_length=6)
    phone = models.CharField(max_length=20)
    note = models.CharField(max_length=200)
    memo = models.CharField(max_length=200)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_verify_proxy'


class UserVipexpLog(models.Model):
    user_id = models.IntegerField()
    before_exp = models.DecimalField(max_digits=10, decimal_places=2)
    def_exp = models.DecimalField(max_digits=10, decimal_places=2)
    after_exp = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_vipexp_log'


class UserWinlose(models.Model):
    date = models.DateField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    up_user_id = models.IntegerField(blank=True, null=True)
    up_username = models.CharField(max_length=255, blank=True, null=True)
    game_kinds_id = models.IntegerField()
    game_kinds_skey = models.CharField(max_length=50)
    income = models.CharField(max_length=20)
    outgo = models.CharField(max_length=20)
    bet = models.CharField(max_length=20)
    winlose = models.CharField(max_length=20)
    prize = models.CharField(max_length=20)
    real_winlose = models.CharField(max_length=20)
    activity_reward = models.CharField(max_length=20)
    returnpoint = models.CharField(db_column='returnPoint', max_length=20)  # Field name made lowercase.
    count = models.IntegerField()
    win = models.IntegerField()
    platform = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_winlose'


class UserWinloseLive(models.Model):
    date = models.DateField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=60)
    up6_id = models.IntegerField()
    up6_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up6_war = models.DecimalField(max_digits=5, decimal_places=2)
    up6_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up6_result = models.DecimalField(max_digits=15, decimal_places=6)
    up6_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up5_id = models.IntegerField()
    up5_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up5_war = models.DecimalField(max_digits=5, decimal_places=2)
    up5_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up5_result = models.DecimalField(max_digits=15, decimal_places=6)
    up5_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up4_id = models.IntegerField()
    up4_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up4_war = models.DecimalField(max_digits=5, decimal_places=2)
    up4_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up4_result = models.DecimalField(max_digits=15, decimal_places=6)
    up4_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up3_id = models.IntegerField()
    up3_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up3_war = models.DecimalField(max_digits=5, decimal_places=2)
    up3_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up3_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up3_result = models.DecimalField(max_digits=15, decimal_places=6)
    up2_id = models.IntegerField()
    up2_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up2_war = models.DecimalField(max_digits=5, decimal_places=2)
    up2_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up2_result = models.DecimalField(max_digits=15, decimal_places=6)
    up2_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up1_id = models.IntegerField()
    up1_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up1_war = models.DecimalField(max_digits=5, decimal_places=2)
    up1_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up1_result = models.DecimalField(max_digits=15, decimal_places=6)
    up1_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up0_id = models.IntegerField()
    up0_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up0_war = models.DecimalField(max_digits=5, decimal_places=2)
    up0_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up0_result = models.DecimalField(max_digits=15, decimal_places=6)
    up0_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    playkey = models.CharField(max_length=20)
    tablenum = models.CharField(max_length=20)
    list_id = models.CharField(max_length=30)
    income = models.DecimalField(max_digits=20, decimal_places=6)
    outgo = models.DecimalField(max_digits=20, decimal_places=6)
    bet = models.DecimalField(max_digits=20, decimal_places=6)
    betok = models.DecimalField(max_digits=20, decimal_places=6)
    money_ok = models.FloatField()
    wl_ok = models.FloatField()
    wait = models.DecimalField(max_digits=20, decimal_places=6)
    winlose = models.DecimalField(max_digits=20, decimal_places=6)
    prize = models.DecimalField(max_digits=20, decimal_places=6)
    activity_reward = models.DecimalField(max_digits=20, decimal_places=6)
    returnpoint = models.DecimalField(db_column='returnPoint', max_digits=20, decimal_places=6)  # Field name made lowercase.
    real_winlose = models.DecimalField(max_digits=20, decimal_places=6)
    bmoney = models.DecimalField(max_digits=20, decimal_places=6)
    count = models.IntegerField()
    bcount = models.IntegerField()
    win = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_winlose_live'


class UserWinloseSport(models.Model):
    date = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=60)
    gtype = models.CharField(max_length=20)
    gtypes = models.CharField(max_length=20)
    rtype = models.CharField(max_length=30)
    bet = models.DecimalField(max_digits=20, decimal_places=6)
    betok = models.DecimalField(max_digits=20, decimal_places=6)
    wait = models.DecimalField(max_digits=20, decimal_places=6)
    winlose = models.DecimalField(max_digits=20, decimal_places=6)
    prize = models.DecimalField(max_digits=20, decimal_places=6)
    wgold = models.DecimalField(max_digits=20, decimal_places=6)
    result = models.DecimalField(max_digits=20, decimal_places=6)
    count = models.IntegerField()
    win = models.IntegerField()
    up6_id = models.IntegerField()
    up6_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up6_war = models.DecimalField(max_digits=5, decimal_places=2)
    up6_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up6_result = models.DecimalField(max_digits=15, decimal_places=6)
    up6_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up5_id = models.IntegerField()
    up5_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up5_war = models.DecimalField(max_digits=5, decimal_places=2)
    up5_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up5_result = models.DecimalField(max_digits=15, decimal_places=6)
    up5_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up4_id = models.IntegerField()
    up4_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up4_war = models.DecimalField(max_digits=5, decimal_places=2)
    up4_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up4_result = models.DecimalField(max_digits=15, decimal_places=6)
    up4_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up3_id = models.IntegerField()
    up3_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up3_war = models.DecimalField(max_digits=5, decimal_places=2)
    up3_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up3_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up3_result = models.DecimalField(max_digits=15, decimal_places=6)
    up2_id = models.IntegerField()
    up2_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up2_war = models.DecimalField(max_digits=5, decimal_places=2)
    up2_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up2_result = models.DecimalField(max_digits=15, decimal_places=6)
    up2_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up1_id = models.IntegerField()
    up1_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up1_war = models.DecimalField(max_digits=5, decimal_places=2)
    up1_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up1_result = models.DecimalField(max_digits=15, decimal_places=6)
    up1_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    up0_id = models.IntegerField()
    up0_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up0_war = models.DecimalField(max_digits=5, decimal_places=2)
    up0_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up0_result = models.DecimalField(max_digits=15, decimal_places=6)
    up0_upgive = models.DecimalField(max_digits=20, decimal_places=6)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_winlose_sport'


class UserWinloseSsc(models.Model):
    date = models.DateField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=60)
    up6_id = models.IntegerField()
    up6_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up6_war = models.DecimalField(max_digits=5, decimal_places=2)
    up6_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up6_result = models.DecimalField(max_digits=15, decimal_places=6)
    up6_upgive = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    up5_id = models.IntegerField()
    up5_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up5_war = models.DecimalField(max_digits=5, decimal_places=2)
    up5_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up5_result = models.DecimalField(max_digits=15, decimal_places=6)
    up5_upgive = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    up4_id = models.IntegerField()
    up4_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up4_war = models.DecimalField(max_digits=5, decimal_places=2)
    up4_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up4_result = models.DecimalField(max_digits=15, decimal_places=6)
    up4_upgive = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    up3_id = models.IntegerField()
    up3_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up3_war = models.DecimalField(max_digits=5, decimal_places=2)
    up3_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up3_result = models.DecimalField(max_digits=15, decimal_places=6)
    up3_upgive = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    up2_id = models.IntegerField()
    up2_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up2_war = models.DecimalField(max_digits=5, decimal_places=2)
    up2_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up2_result = models.DecimalField(max_digits=15, decimal_places=6)
    up2_upgive = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    up1_id = models.IntegerField()
    up1_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up1_war = models.DecimalField(max_digits=5, decimal_places=2)
    up1_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up1_result = models.DecimalField(max_digits=15, decimal_places=6)
    up1_upgive = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    up0_id = models.IntegerField()
    up0_wl = models.DecimalField(max_digits=5, decimal_places=2)
    up0_war = models.DecimalField(max_digits=5, decimal_places=2)
    up0_wgold = models.DecimalField(max_digits=15, decimal_places=6)
    up0_result = models.DecimalField(max_digits=15, decimal_places=6)
    up0_upgive = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    playkey = models.CharField(max_length=20)
    list_id = models.CharField(max_length=30)
    income = models.DecimalField(max_digits=20, decimal_places=6)
    outgo = models.DecimalField(max_digits=20, decimal_places=6)
    bet = models.DecimalField(max_digits=20, decimal_places=6)
    betok = models.DecimalField(max_digits=20, decimal_places=6)
    wait = models.DecimalField(max_digits=20, decimal_places=6)
    winlose = models.DecimalField(max_digits=20, decimal_places=6)
    prize = models.DecimalField(max_digits=20, decimal_places=6)
    activity_reward = models.DecimalField(max_digits=20, decimal_places=6)
    returnpoint = models.DecimalField(db_column='returnPoint', max_digits=20, decimal_places=6)  # Field name made lowercase.
    real_winlose = models.DecimalField(max_digits=20, decimal_places=6)
    bmoney = models.DecimalField(max_digits=20, decimal_places=6)
    count = models.IntegerField()
    bcount = models.IntegerField()
    win = models.IntegerField()
    pay = models.IntegerField()
    pay_total = models.IntegerField()
    withdrawal = models.IntegerField()
    withdrawal_total = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_winlose_ssc'


class Vip(models.Model):
    level = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    needexp = models.IntegerField(db_column='needExp')  # Field name made lowercase.
    daywithdrawaltimes = models.IntegerField(db_column='dayWithdrawalTimes')  # Field name made lowercase.
    dayloginfreedartstimes = models.IntegerField(db_column='dayLoginFreeDartsTimes')  # Field name made lowercase.
    maxdartstimes = models.IntegerField(db_column='maxDartsTimes')  # Field name made lowercase.
    loginaddscore = models.IntegerField(db_column='loginAddScore')  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vip'
