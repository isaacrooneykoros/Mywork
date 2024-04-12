from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def iconremix(request):
    return render(request, 'icons-remix.html')


def iconboxicons(request):
    return render(request, 'icons-boxicons.html')


def iconbootstrap(request):
    return render(request, 'icons-bootstrap.html')


def formsvalidation(request):
    return render(request, 'forms-validation.html')


def chartsapexcharts(request):
    return render(request, 'charts-apexcharts.html')


def chartsecharts(request):
    return render(request, 'charts-echarts.html')


def chartsplot(request):
    return render(request, 'charts-chartjs.html')


def componentsaccordion(request):
    return render(request, 'components-accordion.html')


def componentsalaerts(request):
    return render(request, 'components-alerts.html')


def componentsplot(request):
    return render(request, 'components-progress.html')


def componentscharts(request):
    return render(request, 'components-carousel.html')


def componentsbadges(request):
    return render(request, 'components-badges.html')


def componentsbreadcrumbs(request):
    return render(request, 'components-breadcrumbs.html')


def componentbuttons(request):
    return render(request, 'components-carousel.html')


def components(request):
    return render(request, 'components-carousel.html')


def componentspagination(request):
    return render(request, 'components-pagination.html')


def componentsprogress(request):
    return render(request, 'components-progress.html')


def componentsspinners(request):
    return render(request, 'components-spinners.html')


def componentstabs(request):
    return render(request, 'components-tabs.html')


def componentstooltips(request):
    return render(request, 'components-tooltips.html')


def formseditors(request):
    return render(request, 'forms-editors.html')


def formslayouts(request):
    return render(request, 'forms-layouts.html')


def formselements(request):
    return render(request, 'forms-elements.html')


def componentsmodal(request):
    return render(request, 'components-modal.html')


def componentslistgroup(request):
    return render(request, 'components-list-group.html')


def componentscarousel(request):
    return render(request, 'components-carousel.html')


def componentscards(request):
    return render(request, 'components-cards.html')


def componentsbutton(request):
    return render(request, 'components-buttons.html')


def componentsalerts(request):
    return render(request, 'components-alerts.html')


def chartschartjs(request):
    return render(request, 'charts-chartjs.html')


def chartapexcharts(request):
    return render(request, 'charts-apexcharts.html')


def userprofile(request):
    return render(request, 'users-profile.html')


def tablesgeneral(request):
    return render(request, 'tables-general.html')


def tablesdata(request):
    return render(request, 'tables-data.html')


def pageslogin(request):
    return render(request, 'pages-login.html')


def pagesfaq(request):
    return render(request, 'pages-faq.html')


def pageserror(request):
    return render(request,'pages-error-404.html')


def pagescontact(request):
    return render(request, 'pages-contact.html')


def pagesblank(request):
    return render(request, 'pages-blank.html')
