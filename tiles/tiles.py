from tiles.street import Street

tiles = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    Street(
        position=8,
        color="#09C",
        full_name="Vermont Avenue",
        split_name="Vermont\nAvenue",
        cost=100,
        rent=[6, 30, 90, 270, 400, 550, ],
        type='Street',
        ownerId='0',
        level=2,
        house_cost=50,
        isMortgaged=False,
    )
]
