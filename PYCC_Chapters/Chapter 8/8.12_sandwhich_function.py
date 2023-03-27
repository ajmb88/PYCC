def build_sandwhich(bread, size, *toppings):
    """Build a sandwhich dictionary."""
    print(f"\nMaking a {size.title()} sandwhich with {bread.title()} bread, "
          f"and {toppings} for toppings.")

build_sandwhich('rye', 'large', 'tomatoes', 'bacon', 'turkey', 'ham', 'mayo', 'mustard')

build_sandwhich('whole wheat', 'medium', 'salt n pepper', 'mustard', 'ketchup',
                'french fries', 'pepperoni', 'jam')

build_sandwhich('pumpernickel', 'tripple decker', 'turkey', 'mustard', 'jam', 'crayon',
                'pepsi residue', 'cocaine', 'lettuce')