from django.db import models
from common.models import COMMON


# 立候補者テーブル
class CANDIDATE(COMMON):
    class Meta:
        verbose_name ="立候補者"
        verbose_name_plural ="立候補者"
    
    name = models.CharField(verbose_name='立候補者名', max_length=20)
    nameKN = models.CharField(verbose_name='立候補者名カナ', max_length=40)
    SEX_CHOICES = (
        (0, '男性'),
        (1, '女性'),
        (2, 'other'),
        )
    sex = models.PositiveSmallIntegerField(verbose_name='性別', choices=SEX_CHOICES)
    birthYMD = models.DateField(verbose_name='生年月日')
    BLOOD_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB'),
        ('不明','不明')
        )
    bloodType = models.CharField(verbose_name='血液型', choices=BLOOD_CHOICES, max_length=3, default='不明')
    hobby = models.CharField(verbose_name='趣味', blank=True, null=True,max_length=20)
    partyCd = models.ForeignKey('PARTY', on_delete=models.SET_NULL, verbose_name='所属', blank=True, null=True)
    mail = models.EmailField(verbose_name='メールアドレス', blank=True, null=True)
    link = models.URLField(verbose_name='リンク', blank=True, null=True)
    profile = models.CharField(verbose_name='プロフィール', blank=True, null=True, max_length=140)
    comment1 = models.CharField(verbose_name='コメント1',blank=True, null=True,max_length=50)
    comment2 = models.CharField(verbose_name='コメント2',blank=True, null=True,max_length=50)
    comment3 = models.CharField(verbose_name='コメント3',blank=True, null=True,max_length=50)
    icon = models.ImageField(verbose_name='アイコン', blank=True, null=True)
    image_dtl = models.ImageField(verbose_name='詳細画像', blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    

# 政党テーブル
class PARTY(COMMON):
    class Meta:
        verbose_name ="政党"
        verbose_name_plural ="政党"
        
    partyName = models.CharField(verbose_name='政党名', max_length=20)
    partyNameKN = models.CharField(verbose_name='政党名カナ', max_length=40)
    
    def __str__(self):
        return str(self.partyName)

# 選挙テーブル
class ELECTION(COMMON):
    class Meta:
        verbose_name ="選挙"
        verbose_name_plural ="選挙"
        
    electionCd = models.PositiveSmallIntegerField(verbose_name='選挙コード')
    candidateCd = models.ForeignKey('CANDIDATE', on_delete=models.CASCADE, verbose_name='立候補者')
    areaCd = models.ForeignKey('AREA', on_delete=models.SET_NULL, verbose_name='選挙区', blank=True, null=True)
    electionName = models.CharField(verbose_name='選挙名', max_length=20)
    electionNameKana = models.CharField(verbose_name='選挙名カナ', max_length=40)
    startYMD = models.DateField(verbose_name='開始日')
    endYMD = models.DateField(verbose_name='終了日')
    topPageFLG = models.BooleanField(verbose_name='トップページフラグ', default=False)
    
    def __str__(self):
        return str(self.electionName)

# 選挙区テーブル
class AREA(COMMON):
    class Meta:
        verbose_name ="選挙区"
        verbose_name_plural ="選挙区"
        
    areaName = models.CharField(verbose_name='選挙区名', max_length=20)
    areaNameKana = models.CharField(verbose_name='選挙区名カナ', max_length=40)
    
    def __str__(self):
        return str(self.areaName)
    
# 投票テーブル
class VOTE(COMMON):
    class Meta:
        verbose_name ="投票"
        verbose_name_plural ="投票"
        
    candidateCd = models.ForeignKey('CANDIDATE', on_delete=models.CASCADE, verbose_name='立候補者')
    totalCount = models.PositiveIntegerField(verbose_name='得票数', default=0)
    maleCount = models.PositiveIntegerField(verbose_name='男性得票数', default=0)
    femaleCount = models.PositiveIntegerField(verbose_name='女性得票数', default=0)
    underEighteenCount = models.PositiveIntegerField(verbose_name='未成年得票数', default=0)
    overEighteenCount = models.PositiveIntegerField(verbose_name='成年得票数', default=0)
    lastrank = models.PositiveIntegerField(verbose_name='前回順位', default=0)
    
    def __str__(self):
        return str(self.candidateCd.name)
    
# 画像テーブル
class IMAGE(COMMON):
    class Meta:
        verbose_name ="画像"
        verbose_name_plural ="画像"
    
    candidateCd = models.ForeignKey('CANDIDATE', on_delete=models.CASCADE, verbose_name='立候補者')
    image = models.ImageField(verbose_name='画像ファイル')
    
    def __str__(self):
        return str(self.candidateCd.name)
        
# コメントテーブル        
class COMMENTS(COMMON):
    class Meta:
        verbose_name ="コメント"
        verbose_name_plural ="コメント"
    cmt_id = models.PositiveIntegerField(verbose_name='コメントID' ,default=9999999)
    cmt_user = models.CharField(verbose_name='名前', max_length=20)
    cmt_text = models.TextField(verbose_name='本文',max_length=400)
    cmt_good = models.PositiveIntegerField(verbose_name='good' ,default=0)
    cmt_bad = models.PositiveIntegerField(verbose_name='bad' ,default=0)
    # cmt_parent = models.IntegerField(verbose_name='親コメント')
    posted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cmt_text