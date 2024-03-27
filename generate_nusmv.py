def generate_nusmv_code(obstacle_count):
    distances = ', '.join([f'd_{50 * i}' for i in range(2 * obstacle_count + 1)])
    obstacle_defs = ', '.join([f'obst_{i + 1}' for i in range(obstacle_count)])

    # Correctly generate movement cases without referencing undefined distances
    movement_cases = [
        'aircraft_movement = stop & distance = d_0 : move_forward;',
    ] + [
        f'aircraft_movement = move_forward & distance = d_{50 * i} : {{move_forward, turn_right}};' for i in range(1, 2 * obstacle_count, 2)
    ] + [
        f'aircraft_movement = move_forward & distance = d_{50 * i} & obstacles = obst_{(i+1)//2}: stop;' for i in range(2, 2 * obstacle_count, 2)
    ] + [
        'aircraft_movement = turn_right : move_forward;',
        f'aircraft_movement = move_forward & distance = d_{50 * 2 * obstacle_count} & obstacles != obst_{obstacle_count}: take_off;',
        'aircraft_movement = take_off : take_off;',
        'TRUE : aircraft_movement;'
    ]

    distance_cases = [
        f'aircraft_movement = move_forward & distance = d_{50 * i} : d_{50 * (i + 1)};' for i in range(2 * obstacle_count)
    ] + [
        f'aircraft_movement = turn_right & distance = d_{50 * i} : d_{50 * (i + 1)};' for i in range(1, 2 * obstacle_count, 2)
    ] + [
        'TRUE : distance;'
    ]

    obstacle_cases = [
        f'aircraft_movement = move_forward & distance = d_{50 * i} : obst_{(i+1)//2};' for i in range(2, 2 * obstacle_count, 2)
    ] + [
        'TRUE : obstacles;'
    ]

    movement_cases_str = '\n    '.join(movement_cases)
    distance_cases_str = '\n    '.join(distance_cases)
    obstacle_cases_str = '\n    '.join(obstacle_cases)

    return f"""MODULE main
VAR
  aircraft_movement: {{turn_right, move_forward, stop, take_off}};
  distance: {{{distances}}};
  obstacles: {{none, {obstacle_defs}}};

ASSIGN
  init(aircraft_movement) := stop;
  init(distance) := d_0;
  init(obstacles) := none;
  
  next(aircraft_movement) :=
  case
    {movement_cases_str}
  esac;

  next(distance) :=
  case
    {distance_cases_str}
  esac;

next(obstacles) :=
  case
    {obstacle_cases_str}
  esac;
    
CTLSPEC
  EF(aircraft_movement = take_off);

CTLSPEC
  EG(aircraft_movement = move_forward | aircraft_movement = stop | aircraft_movement = turn_right | aircraft_movement = take_off);

CTLSPEC
  EF(aircraft_movement = stop);

CTLSPEC
  EF(distance = d_50);
"""

obstacle_counts = [3, 5, 7, 10, 15, 20]

for count in obstacle_counts:
    code = generate_nusmv_code(count)
    file_name = f"nusmv_obstacles_{count}.smv"
    with open(file_name, "w") as file:
        file.write(code)
    print(f"File {file_name} generated.")
