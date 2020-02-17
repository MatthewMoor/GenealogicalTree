from django.shortcuts import render
from datatree.models import People, Relation
from datatree.forms import AppendPeople, AppendChild, TakeIdForm, DeleteForm
from django.http import Http404

def show_tree(request):
    form_id = TakeIdForm()
    form_node = AppendPeople()
    form_child = AppendChild()
    form_delete = DeleteForm()

    if request.method == 'POST':
        if "append_node" in request.POST:
            form_node = AppendPeople(request.POST)
            if form_node.is_valid():
                person = Relation.objects.create(
                    person=form_node.cleaned_data['name']
                )
                person.save()

        if "append_child" in request.POST:
            form_id = TakeIdForm(request.POST)
            try:
                if form_id.is_valid():
                    child_node = Relation.objects.get(id=form_id.cleaned_data.get("child_id"))
                    parent_node = Relation.objects.get(id=form_id.cleaned_data.get("parent_id"))
                    child_node.move_to(parent_node,position="first-child")
            except Relation.DoesNotExist:
                raise Http404

        if "DeleteButton" in request.POST:
            form_delete = DeleteForm(request.POST)
            try:
                if form_delete.is_valid():
                        object_pk = Relation.objects.get(pk=form_delete.cleaned_data.get("child_id")).get_root()
                        object_pk.delete()
            except Relation.DoesNotExist:
                raise Http404

    context = {
        'genres': Relation.objects.all(),
        'form_node': form_node,
        'form_child': form_child,
        'form_id': form_id,
        'form_delete': form_delete,
    }
    return render(request, "tree.html", context)