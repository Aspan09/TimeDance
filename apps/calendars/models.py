from django.db import models


class Actual(models.Model):

    image = models.ImageField(verbose_name='Fotos aktuell', blank=True, upload_to='resource')
    title = models.CharField(verbose_name='Vergaldungen', max_length=255, blank=True)
    content = models.TextField(verbose_name="Inhalt", max_length=5000)
    button = models.CharField(verbose_name='Schaltfläche', max_length=100, blank=True)
    link = models.CharField(verbose_name='Der Link', max_length=1000, blank=True)

    class Meta:
        verbose_name = "Aktuelle"
        verbose_name_plural = "Aktuelles"

    def __str__(self):
        return self.title


class ActualButtonOne(models.Model):
    title = models.CharField(verbose_name='Vergaldungen', max_length=255, blank=True)
    content = models.TextField(verbose_name='Inhalt', max_length=5000)
    link = models.CharField(verbose_name='Der Link', max_length=1000, blank=True)

    class Meta:
        verbose_name = "weitere Nachrichten Nr.1"
        verbose_name_plural = "weitere Nachrichten Nr.1"

    def __str__(self):
        return self.title


class ActualButtonTwo(models.Model):
    title = models.CharField(verbose_name='Vergaldungen', max_length=255, blank=True)
    content = models.TextField(verbose_name='Inhalt', max_length=5000)
    link = models.CharField(verbose_name='Der Link', max_length=1000, blank=True)

    class Meta:
        verbose_name = "weitere Nachrichten Nr.2"
        verbose_name_plural = "weitere Nachrichten Nr.2"

    def __str__(self):
        return self.title


class ActualButtonThird(models.Model):
    title = models.CharField(verbose_name='Vergaldungen', max_length=255, blank=True)
    content = models.TextField(verbose_name='Inhalt', max_length=5000)
    link = models.CharField(verbose_name='Der Link', max_length=1000, blank=True)

    class Meta:
        verbose_name = "weitere Nachrichten Nr.3"
        verbose_name_plural = "weitere Nachrichten Nr.3"

    def __str__(self):
        return self.title


class ActualButtonFourth(models.Model):
    title = models.CharField(verbose_name='Vergaldungen', max_length=255, blank=True)
    content = models.TextField(verbose_name='Inhalt', max_length=5000)
    link = models.CharField(verbose_name='Der Link', max_length=1000, blank=True)

    class Meta:
        verbose_name = "weitere Nachrichten Nr.4"
        verbose_name_plural = "weitere Nachrichten Nr.4"

    def __str__(self):
        return self.title


class ActualButtonFifth(models.Model):
    title = models.CharField(verbose_name='Vergaldungen', max_length=255, blank=True)
    content = models.TextField(verbose_name='Inhalt', max_length=5000)
    link = models.CharField(verbose_name='Der Link', max_length=1000, blank=True)

    class Meta:
        verbose_name = "weitere Nachrichten Nr.5"
        verbose_name_plural = "weitere Nachrichten Nr.5"

    def __str__(self):
        return self.title


class Monday(models.Model):

    time = models.CharField(verbose_name='Zeit', blank=True)
    numbers = models.CharField(verbose_name='Zahl', blank=True)
    name_of_the_teachers = models.TextField(verbose_name='Name der Lehrer', max_length=200, blank=True)

    class Meta:
        verbose_name = "Montag"
        verbose_name_plural = "Montage"


class Tuesday(models.Model):

    time = models.CharField(verbose_name='Zeit', blank=True)
    numbers = models.CharField(verbose_name='Zahl', blank=True)
    name_of_the_teachers = models.TextField(verbose_name='Name der Lehrer', max_length=200, blank=True)

    class Meta:
        verbose_name = "Dienstag"
        verbose_name_plural = "Dienstage"


class Wednesday(models.Model):

    time = models.CharField(verbose_name='Zeit', blank=True)
    numbers = models.CharField(verbose_name='Zahl', blank=True)
    name_of_the_teachers = models.TextField(verbose_name='Name der Lehrer', max_length=200, blank=True)

    class Meta:
        verbose_name = "Mittwoch"
        verbose_name_plural = "Medien"


class Thursday(models.Model):

    time = models.CharField(verbose_name='Zeit', blank=True)
    numbers = models.CharField(verbose_name='Zahl', blank=True)
    name_of_the_teachers = models.TextField(verbose_name='Name der Lehrer', max_length=200, blank=True)

    class Meta:
        verbose_name = "Donnerstag"
        verbose_name_plural = "Donnerstage"


class Friday(models.Model):

    time = models.CharField(verbose_name='Zeit', blank=True)
    numbers = models.CharField(verbose_name='Zahl', blank=True)
    name_of_the_teachers = models.TextField(verbose_name='Name der Lehrer', max_length=200, blank=True)

    class Meta:
        verbose_name = "Freitag"
        verbose_name_plural = "Freitage"


class Saturday(models.Model):

    time = models.CharField(verbose_name='Zeit', blank=True)
    numbers = models.CharField(verbose_name='Zahl', blank=True)
    name_of_the_teachers = models.TextField(verbose_name='Name der Lehrer', max_length=200, blank=True)

    class Meta:
        verbose_name = "Samstag"
        verbose_name_plural = "Samstage"





