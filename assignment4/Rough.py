Cast.objects.values('movie__movie_id').annotate(Count('role',distinct=True))