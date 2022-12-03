from django.shortcuts import render

from front import Process_data_ifre


# Create your views here.
def home(request):
    return_dict = Process_data_ifre.get_total_jobs()
    context = {
        
    }
    return render(request, "template", context)

# Wishlist
# les métier liké

# Coup de coeur
# retour algo
# liste des métiers + infos
# listes des formations correspondantes

# une route pour afficher ele premier onboarding

# une route pour l'api des info
