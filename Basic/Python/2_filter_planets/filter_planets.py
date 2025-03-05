def shorten_planets(planets:list)->list:
    """
    Filters a list of planet names, returning only those with fewer than 6 characters.

    Parameters:
    planets (list): A list of planet names as strings.

    Returns:
    list: A list containing only the planet names that have fewer than 6 characters.

    Example:
    >>> shorten_planets(["Mars", "Earth", "Venus", "Jupiter"])
    ['Mars', 'Venus']
    """
    filter_planets = []
    if len(planets) > 0:
        for planet in planets:
            if len(planet) < 6:
                filter_planets.append(planet)
    return filter_planets
        