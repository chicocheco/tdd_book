# The Outside-in approach

We specify the API we want from the code at the layers below

> Write an FT with the user's story

> Write minimal code change in the existing templates (e.g. adding links to the navbar)

> Run the FT

> Moving down one layer: View functions (the controller)
> 1. Add a unittest (1) for a new template (MyLists)
> 2. Add a new URL pattern for this template
> 3. Add a new view of this URL pattern
> 4. Modify the pre-existing templates to be compatible with this one 
>(extending base.html, blocks..., placeholder template (2))

> Run the FT

> Refactor templates
> 1. Restructuring template inheritance hierarchy (playing around with blocks)
> 2. Placeholder template (2) converted to a standard template with API we wish to use later (models)

> (Passing unittests) Commit: "url, placeholder view, and first-cut templates for my_lists"

> Moving down to the next layer: What the view passes to the template
> 1. Add a unittest for giving correct objects (e.g. owner) to the template (MyLists)
> 2. Modify the view, passing correct objects to the template
> 3. Modify the unittest (1) to include it, creating correct objects to pass to the template

> The next "Requirement" from the Views layer: New lists should record owner
> 1. Add a unittest "test_list_owner_is_saved_if_user_is_authenticated"
> 2. Modify the view according to this test
> 3. Failing test... We decide whether continue or rewrite the tests using mocks (here we continue)

> (Failing unittests) Commit: "new_list view tries to assign owner but cant", Tag: revisit_this_point_with_isolated_tests

> Moving down to the next layer: Model Layer
> 1. Add a unittest for that the lists can have owners (ListModelTest)
> 2. Modify the model according to this test
> 3. Add another unittest for that the lists can have owners but do not have too!
> 4. Modify the model according to this test
> 5. Make migrations
> 6. Modify the old "new_list" view to consider .owner attribute (property)

> (Passing unittest) Commit: "lists can have owners, which are saved on creation."

> Final step: Feeding through the .name API from the template (my lists)
> 1. Add a unittest for that the list uses the first item (from Item) for .name attribute
> 2. Modify the model according to this test, use @property decorator

> Commit: "implement .name attribute of list"