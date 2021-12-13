class Element:
    t_melting = 0
    t_sprays = 0
    kelv_t_melting = t_melting + 273.15
    kelv_t_sprays = t_sprays + 273.15
    far_t_melting = (t_melting * 9 / 5) + 32
    far_t_sprays = (t_sprays * 9 / 5) + 32

    def agg_state(self, t):

        if t >= self.t_melting and t <= self.t_sprays:
            print("Железо расплавилось!")
        elif t < self.t_melting:
            print("Железо твердое!")
        elif t >= self.t_sprays:
            print("Железо испарилось!")

    def Kel(self, t):

        if t >= self.kelv_t_melting and t <= self.kelv_t_sprays:
            print("Железо расплавилось!")
        elif t < self.kelv_t_melting:
            print("Железо твердое!")
        elif t >= self.kelv_t_sprays:
            print("Железо испарилось!")

    def Far(self, t):

        if t >= self.far_t_melting and t <= self.far_t_sprays:
            print("Железо расплавилось!")
        elif t < self.far_t_melting:
            print("Железо твердое!")
        elif t >= self.far_t_sprays:
            print("Железо испарилось!")

class Iron(Element):
    t_melting = 1538
    t_sprays = 2862
    kelv_t_melting = t_melting + 273.15
    kelv_t_sprays = t_sprays + 273.15
    far_t_melting = (t_melting * 9 / 5) + 32
    far_t_sprays = (t_sprays * 9 / 5) + 32


Fe = Iron()
Fe.agg_state(1500)
Fe.Kel(2000)
Fe.Far(2300)
