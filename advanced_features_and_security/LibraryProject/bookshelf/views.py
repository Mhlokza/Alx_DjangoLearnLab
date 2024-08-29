from django.shortcuts import render
def edit(request):
    @permission_required('bookshelf.can_edit', raise_exception=True)

else:
    raise raise_exception("you have no permission")
