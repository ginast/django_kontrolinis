from django.contrib import admin
from .models import Game, Publisher, GameReview



class GameReviewAdmin(admin.ModelAdmin):
    list_display = ('game','reviewer','date_created') #pridejus review_content uzlusta programa 
   

admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(GameReview, GameReviewAdmin)
