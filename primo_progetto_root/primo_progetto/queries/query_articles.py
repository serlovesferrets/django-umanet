from news.models import Article, Journalist

a1 = Article(title="Primo articolo", contents="lorem ipsum dolor sit amen")

# g3 come foreign key
g3 = Journalist.objects.get(id=3)
a1.journalist = g3
a1.save()

print(g3)
print(a1)
print(a1.journalist)

# stessa foreign key
a2 = Article(title="Secondo articolo", contents="Il mio secondo articolo")
a2.journalist = g3
a2.save()

print(Article.objects.all())

# articoli in cui giornalista = g3
print(Article.objects.filter(journalist=g3))

# articoli di g3
print(g3.articles.all())
