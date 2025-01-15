from typing import Optional
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Article, Journalist


def _home_without_templates(request: HttpRequest):
    articles_str = "<br>".join([article.title for article in Article.objects.all()])
    journalists_str = "<br>".join([
        journalist.last_name for journalist in Journalist.objects.all()
    ])

    return HttpResponse(f"""
    <br>Articoli:<br>
    {articles_str}

    <br>Giornalisti:<br>
    {journalists_str}
    """)


def home(request: HttpRequest):
    articles = Article.objects.all()
    journalists = Journalist.objects.all()
    context = {"articoli": articles, "giornalisti": journalists}
    print(context)
    return render(request, "homepage.html", context)


def article_detail(request: HttpRequest, pk: int):
    article = get_object_or_404(Article, pk=pk)
    context = {"article": article}
    return render(request, "article_detail.html", context)


def list_articles(request: HttpRequest, pk: Optional[int] = None):
    if not pk:
        articles = Article.objects.all()
        context = {"articles": articles}

        return render(request, "all_articles.html", context)

    journalist = get_object_or_404(Journalist, pk=pk)
    articles = Article.objects.filter(journalist=journalist)
    context = {"journalist": journalist, "articles": articles}

    return render(request, "journalist_articles.html", context)
