from news.models import Journalist

# select * from Journalists
print(Journalist.objects.all())

# insert into Journalists values ('Mario', 'Rossi')
g1 = Journalist(first_name="Mario", last_name="Rossi")
g1.save

# idem
g2 = Journalist(first_name="Pinco", last_name="Pallino")

# update Journalists set last_name = 'Pallo' where id = 2
g2.last_name = "Pallo"
g2.save()

print(g1)
print(g2.first_name)

g3 = Journalist(first_name="Mario", last_name="Bianchi")
g3.save()

print(g3)

_ = Journalist.objects.create(first_name="Nome", last_name="Cognome")

print(g1.id)
print(g3.id)
print(g2.pk)

# select * from Journalists where pk = 1
print(Journalist.objects.get(pk=1))

# select * from Journalists where first_name = 'Mario'
print(Journalist.objects.filter(first_name="Mario"))

print(Journalist.objects.all())

journalists = Journalist.objects.all()
print(journalists)

# select * from Journalists where first_name <> 'Mario'
print(Journalist.objects.exclude(last_name="Rossi"))

# select name from Journalists
for g in journalists:
    print(g.first_name)

# update Journalists set 
#   last_name = 'Guido',
#   first_name = 'Guido'
# where pk = 1
g4 = Journalist.objects.get(pk=1)
g4.first_name = "Guido"
g4.last_name = "Guidi"
g4.save()

print(Journalist.objects.all())

# delete from Journalists where pk = 1
g4 = Journalist.objects.get(pk=1)
g4.delete()

print(Journalist.objects.all())
