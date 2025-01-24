from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Category, Movie, MovieShots, Rating, RatingStar, Actor, Genre, Reviews

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Категория
    list_display = ('id', 'name', 'url')
    list_display_links = ('name', )

class ReviewInline(admin.TabularInline):
    # Отзывы на странице фильма
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)


    def get_image(self, obj):
        return mark_safe(f"<image src={obj.image.url} width=50, height=50")

    get_image.shots_description = 'Изображение'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Фильмы
    list_display = ('id', 'category', 'title', 'year','draft')
    list_display_links = ('title', )
    list_filter = ('category', 'year' )
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    readonly_fields = ('get_image',)
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'), )
    fieldsets = (
        (None, {
                'fields': (('title', 'tagline', 'year', 'world_premiere'),)
             }),
        (None, {
            'fields': (('description','category',),)
        }),
        (None, {
            'fields': (('country', 'get_image'),)
        }),
        ('Actors', {
            'classes': ('collapse',),
            'fields': (('directors', 'actors', 'genres'),)
        }),
        ('Budget', {
            'classes': ('collapse',),
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
    )


    def get_image(self, obj):
        return mark_safe(f"<image src={obj.poster.url} width=150, height=150")

    get_image.shots_description = "Постер"



@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    # Отзывы
    list_display = ('name', 'email',)
    readonly_fields = ('name', 'email')
    fieldsets = (
        ('Отправитель', {
            'classes': ('collapse',),
            'fields': (('name', 'email'),)
        }),
        (None, {
            'fields': (('text', 'movie'),)
        }),
    )

@admin.register(Rating)
class Rating(admin.ModelAdmin):
    # Рейтинг
    list_display = ('movie', )


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # Актеры
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)


    def get_image(self, obj):

        return mark_safe(f'<img src={obj.image.url} width="50", height="50"')

    get_image.short_description = 'Изображение'



@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    # Рейтинг
    list_display = ('value', )


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    # Кадры из фильма
    list_display = ('title', 'get_image')
    readonly_fields = ('get_image',)


    def get_image(self,obj):
        return mark_safe(f"<image src={obj.image.url} width=50, height=50")

    get_image.shots_description = 'Изображение'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Жанры
    list_display = ('name',)

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'

