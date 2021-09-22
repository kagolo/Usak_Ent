from.models import(Category)

def get_Categories():
    return Category.objects.all()

def get_Category(Category_id):
    return Category.objects.get(pk=Category_id)
   