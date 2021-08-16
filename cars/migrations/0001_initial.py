# Generated by Django 3.2.6 on 2021-08-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('sedan', 'sedan'), ('suv', 'suv'), ('wagon', 'wagon'), ('wagon', 'wagon'), ('coup', 'coup'), ('hatchback', 'hatchbak'), ('pickup', 'pickup'), ('compact', 'compact'), ('compact', 'compact'), ('sport coupe', 'sport coupe'), ('van', 'van'), ('crossover', 'crossover')], max_length=15)),
                ('color', models.CharField(blank=True, choices=[('red', 'red'), ('yellow', 'yellow'), ('orange', 'orange'), ('green', 'green'), ('blue', 'blue'), ('violet', 'violet'), ('gray', 'gray'), ('white', 'white'), ('black', 'black')], max_length=10)),
                ('transmission', models.CharField(blank=True, choices=[('manual', 'manual'), ('auto', 'auto'), ('robot', 'robot')], max_length=10)),
                ('rul', models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right')], max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=30)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=9)),
                ('price', models.FloatField()),
                ('release_date', models.IntegerField(choices=[(1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021, max_length=4, verbose_name='release date')),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
