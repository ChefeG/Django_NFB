from django.db import models

class ModelNewsLine(models.Model):
    news = models.CharField('News', max_length=100)

    def __str__(self):
        return self.news

    class Meta:
        verbose_name = 'News line'

class ModelСover(models.Model):
    image = models.ImageField(upload_to='Cover/')
    title = models.CharField('Title', max_length=100)
    anons = models.CharField('Anons', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cover'
        verbose_name_plural = 'Covers'

class ModelMatches(models.Model):
    team_1 = models.CharField('Team_1', max_length=50)
    team_2 = models.CharField('Team_2', max_length=50)
    date = models.CharField('Date', max_length=70)
    venue = models.CharField('Venue', max_length=100)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

class ModelTeams(models.Model):
    team = models.CharField('Team', max_length=50)
    win = models.IntegerField('Win')
    draw = models.IntegerField('Draw')
    lose = models.IntegerField('Lose')
    pts = models.IntegerField('Pts')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

class ModelTopPlayer(models.Model):
    image = models.ImageField(upload_to='media/', null=True)
    name = models.CharField('Name', max_length=100, null=True)
    description = models.CharField('Description', max_length=250, null=True)
    birthday = models.CharField('Birthday', max_length=50, null=True)
    location = models.CharField('Location', max_length=50, null=True)
    squad_number = models.IntegerField('Squad_number', null=True)
    club = models.CharField('Club', max_length=50, null=True)
    position = models.CharField('Position', max_length=50, null=True)
    previous_clubs = models.CharField('Clubs', max_length=250, null=True)
    text = models.TextField('Text', null=True)
    blockquote = models.TextField('Blockquote', null=True)

    url = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Top player'
        verbose_name_plural = 'Top players'

class ModelStatistics(models.Model):
    discord_members = models.IntegerField('Discord_members')
    twitter_members = models.IntegerField('Twitter_members')
    nft_in_stake = models.IntegerField('nft_in_stake')

    class Meta:
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistics'


class ModelTopMatches(models.Model):
    team_1_image = models.ImageField(upload_to='TopMatches/')
    team_2_image = models.ImageField(upload_to='TopMatches/')
    vs = models.CharField('Vs', max_length=100)
    description = models.CharField('Description', max_length=250)

    def __str__(self):
        return self.vs

    class Meta:
        verbose_name = 'Top match'
        verbose_name_plural = 'Top matches'

class ModelAnnouncements(models.Model):
    day = models.IntegerField('Day')
    month = models.CharField('Month', max_length=15)
    image = models.ImageField(upload_to='media/', null=True)
    title = models.CharField('Title', max_length=50, null=True)
    author = models.CharField('Author', max_length=25, null=True, default='author')
    description = models.CharField('Description', max_length=250)
    text = models.TextField('Text', null=True)
    blockquote = models.TextField('Blockquote', null=True)

    url = models.SlugField(unique=True, null=True)

    class Meta:
            verbose_name = 'Announcement'
            verbose_name_plural = 'Announcements'








