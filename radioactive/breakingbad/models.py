from django.db import models


class Questions(models.Model):
    questions_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __unicode__(self):
        return '%s, %d' % (self.questions_text, self.pub_date)


class Choice(models.Model):
    questions = models.ForeignKey(Questions)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
