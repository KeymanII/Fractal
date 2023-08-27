import turtle


def make_fractal_gen(gen0, rules, *gen_needed):
    gen0 = list(gen0)
    if not gen_needed:
        gen_needed = 3
    for i in range(gen_needed - 1):
        gen0 = list(gen0)
        for j in range(len(gen0)):
            try:
                gen0[j] = rules[gen0[j]]
            except:
                print('Не указанно правило для символа!', gen0[j])
        gen0 = ''.join(gen0)
    gen_current = ''.join(gen0)
    return gen_current


def draw_fractal_gen(gen, movement_rules, colour):
    sc = turtle.Screen()
    shoopa = turtle.Turtle()
    shoopa.color(colour)
    for el in gen:
            rules = movement_rules[el]
            if 'degree' in rules:
                if rules['degree'][1] == 'right':
                    shoopa.right(rules['degree'][0])
                else:
                    shoopa.left(rules['degree'][0])
            if 'step' in rules:
                if rules['step'][1] == 'f':
                    shoopa.forward(rules['step'][0])
                else:
                    shoopa.backward(rules['step'][0])
    sc.exitonclick()



movement_rule = {'F': {'step': [20, 'f']}, '+': {'degree': [60, 'right']}, '-': {'degree': [60, 'left']}}
rule = {"F": "FF+F-F-FFF-FFF-F-F+FF", '+': '+', '-': '-'}
gen0 = 'F++F-F--F+FF'
color = 'purple'
gen_drawing = make_fractal_gen(gen0, rule)
print(gen_drawing)
draw_fractal_gen(gen_drawing, movement_rule, color)
