from collections import deque
from table import GestorTablaSimbolo


class JSSemantic:

    def __init__(self, gestor_ts):
        self.gestor_ts = gestor_ts
        self.pila_aux = deque()

    def regla_F1(self):  # F -> function H
        self.gestor_ts.zona_decl = True

    def regla_F2(self):  # F -> function H ID (
        id_ = self.pila_aux[-1]
        self.gestor_ts.crea_tabla(id_.pos)

    def regla_F3(self):  # F -> function H ID ( A )
        a = self.pila_aux[-2]
        id_ = self.pila_aux[-4]
        h = self.pila_aux[-5]
        self.gestor_ts.aniadir_funcion_ts(id_.pos, len(a.tipo.split(' ')), a.tipo, h.ret)
        self.gestor_ts.zona_decl = False

    def regla_F4(self):  # F -> function H ID ( A ) { C
        c = self.pila_aux[-1]
        h = self.pila_aux[-7]
        f = self.pila_aux[-9]

        if c.ret == h.tipo:
            f.tipo = 'ok'
        else:
            f.tipo = 'error'

    def regla_F5(self):  # F -> function H ID ( A ) { C }
        self.gestor_ts.libera_tabla()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()

    def regla_C1(self):  # C -> B C1 y C -> S C1
        c1 = self.pila_aux.pop()
        b = self.pila_aux.pop()
        c = self.pila_aux[-1]

        if b.tipo == 'ok' and (c1.tipo == 'ok' or c1.tipo == 'vacio'):
            c.tipo = 'ok'
        elif b.tipo == 'ok':
            c.tipo = c1.tipo
        elif c1.tipo == 'ok':
            c.tipo == b.tipo

        if b.ret == c1.ret:
            c.ret = b.ret
        elif b.ret == 'vacio':
            c.ret = c1.ret
        elif c1.ret == 'vacio':
            c.ret = b.ret
        else:
            c.ret == 'error'

    def regla_C2(self):  # C -> lambda
        c = self.pila_aux[-1]
        c.tipo = 'vacio'
        c.ret = 'vacio'

    def regla_E1(self):  # E -> R Y
        y = self.pila_aux.pop()
        r = self.pila_aux.pop()
        e = self.pila_aux[-1]

        if r.tipo == y.tipo:
            e.tipo = r.tipo
        else:
            e.tipo = 'error'

    def regla_Y(self):  # Y -> || R Y1
        y1 = self.pila_aux.pop()
        r = self.pila_aux.pop()
        self.pila_aux.pop()
        y = self.pila_aux[-1]

        if r.tipo == 'logico' and (y1.tipo == 'logico' or y1.tipo == 'vacio'):
            y.tipo = 'logico'
        else:
            y.tipo = 'error'

    def regla_R(self):  # R -> U I
        i = self.pila_aux.pop()
        u = self.pila_aux.pop()
        r = self.pila_aux[-1]

        if u.tipo == 'logico' and i.tipo == 'logico':
            r.tipo = 'ok'
        elif i.tipo == 'vacio':
            r.tipo = 'error'

    def regla_I(self):  # I -> && U
        u = self.pila_aux.pop()
        self.pila_aux.pop()
        i = self.pila_aux[-1]

        if u.tipo == 'logico':
            i.tipo = u.tipo
        else:
            i.tipo = 'error'

    def regla_U(self):  # U -> V O
        o = self.pila_aux.pop()
        v = self.pila_aux.pop()
        u = self.pila_aux[-1]

        if v.tipo == o.tipo:
            u.tipo = 'logico'
        elif o.tipo == 'vacio':
            u.tipo = v.tipo
        else:
            u.tipo = 'error'

    def regla_O(self):  # O -> != V y O -> == V
        v = self.pila_aux.pop()
        self.pila_aux.pop()
        o = self.pila_aux[-1]

        if v.tipo in ['entero', 'cadena', 'logico']:
            o.tipo = v.tipo
        else:
            o.tipo = 'error'

    def regla_V(self):  # V -> W J
        j = self.pila_aux.pop()
        w = self.pila_aux.pop()
        v = self.pila_aux[-1]

        if w.tipo == 'entero' and (j.tipo == 'entero' or j.tipo == 'vacio'):
            v.tipo = 'entero'
        elif w.tipo == 'cadena' and j.tipo == 'vacio':
            v.tipo = 'cadena'
        elif w.tipo == 'logico' and j.tipo == 'vacio':
            v.tipo = 'logico'
        else:
            v.tipo = 'error'

    def regla_J(self):  # J -> + W J1  y J -> - W J1
        j1 = self.pila_aux.pop()
        w = self.pila_aux.pop()
        self.pila_aux.pop()
        j = self.pila_aux[-1]

        if w.tipo == 'entero' and (j1.tipo == 'entero' or j1.tipo == 'vacio'):
            w.tipo = 'entero'
        else:
            w.tipo = 'error'

    def regla_W1(self):  # W -> ++ ID
        id_ = self.pila_aux.pop()
        self.pila_aux.pop()
        w = self.pila_aux[-1]
        if self.gestor_ts.buscar_simbolo_ts(id_.pos)['tipo'] == 'entero':
            w.tipo = 'ok'
        else:
            w.tipo = 'error'

    def regla_W2(self):  # W -> ( E )
        self.pila_aux.pop()
        e = self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux[-1] = e.tipo

    def regla_W3(self):  # W -> ID D
        d = self.pila_aux.pop()
        id_ = self.pila_aux.pop()
        w = self.pila_aux[-1]
        simbolo = self.gestor_ts.buscar_simbolo_ts(id_.pos)

        if d.tipo == 'vacio':
            w.tipo = simbolo['tipo']
        elif simbolo['tipoParam']:
            w.tipo = simbolo['tipoRetorno']
        else:
            w.tipo = 'error'

    def regla_W4(self):  # W-> entero
        self.pila_aux.pop()
        self.pila_aux[-1].tipo = 'entero'

    def regla_W5(self):  # W-> cadena
        self.pila_aux.pop()
        self.pila_aux[-1].tipo = 'cadena'

    def regla_W67(self):  # W -> true | W -> false
        self.pila_aux.pop()
        self.pila_aux[-1].tipo = 'logico'

    def regla_D(self):  # D -> (L)  ##igual G2
        self.pila_aux.pop()
        l = self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux[-1].tipo = l.tipo

    def regla_B1_1(self):  # B -> let T ID ;
        self.gestor_ts.zona_decl = True

    def regla_B1_2(self):  # B -> let T ID ;
        self.pila_aux.pop()
        id_ = self.pila_aux.pop()
        t = self.pila_aux.pop()
        self.pila_aux.pop()
        b = self.pila_aux[-1]
        self.gestor_ts.aniadir_variable_ts(id_.pos, t.tipo, t.ancho)
        b.tipo = 'ok'
        b.ret = 'vacio'
        self.gestor_ts.zona_decl = False

    def regla_B2(self):  # B -> if ( E ) S {
        s = self.pila_aux.pop()
        self.pila_aux.pop()
        e = self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        b = self.pila_aux[-1]

        if e.tipo == 'logico':
            b.tipo = s.tipo
        else:
            b.tipo = 'error'

    def regla_B3(self):  # B -> for (N;E;M) {C}
        self.pila_aux.pop()
        c = self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        e = self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        b = self.pila_aux[-1]

        if e.tipo == 'logico':
            b.tipo = c.tipo
        else:
            b.tipo = 'error'

    def regla_N1(self):  # N -> ID = E
        e = self.pila_aux.pop()
        self.pila_aux.pop()
        id_ = self.pila_aux.pop()
        n = self.pila_aux[-1]

        if id_.tipo == e.tipo:
            n.tipo = 'ok'
        else:
            n.tipo = 'error'

    def regla_N2(self):  # N -> lambda
        self.pila_aux[-1] = 'ok'

    def regla_M1(self):  # M -> N
        n = self.pila_aux.pop()
        m = self.pila_aux[-1]
        m.tipo = n.tipo

    def regla_M2(self):  # M -> ++ ID
        id_ = self.pila_aux.pop()
        self.pila_aux.pop()
        m = self.pila_aux[-1]

        if id_.tipo == 'entero':
            m.tipo = 'ok'
        else:
            m.tipo = 'error'

    def regla_S1(self):  # S -> ID G ;
        self.pila_aux.pop()
        g = self.pila_aux.pop()
        id_ = self.pila_aux.pop()
        s = self.pila_aux[-1]

        if id_.tipo == 'funcion':
            if id_.tipo_param == g.tipo:
                s.tipo = 'ok'
            else:
                s.tipo = 'error'
        elif id_.tipo == g.tipo:
            s.tipo = 'ok'
        else:
            s.tipo = 'error'

    def regla_S2(self):  # S -> ++ ID ;
        self.pila_aux.pop()
        id_ = self.pila_aux.pop()
        self.pila_aux.pop()
        s = self.pila_aux[-1]

        if id_.tipo == 'entero':
            s.tipo = 'ok'
        else:
            s.tipo = 'error'

    def regla_G1(self):  # G -> = E
        e = self.pila_aux.pop()
        self.pila_aux.pop()
        g = self.pila_aux[-1]
        g.tipo = e.tipo

    def regla_G2(self):  # G -> ( L )
        self.pila_aux.pop()
        ll = self.pila_aux.pop()
        self.pila_aux.pop()
        g = self.pila_aux[-1]
        g.tipo = ll.tipo

    def regla_S1(self):  # S -> input ( ID ) ; y S -> alert ( E ) ;
        self.pila_aux.pop()
        self.pila_aux.pop()
        id_ = self.pila_aux.pop()
        self.pila_aux.pop()
        self.pila_aux.pop()
        s = self.pila_aux[-1]

        if id_.tipo == 'logico':
            s.tipo = 'error'
        else:
            s.tipo = 'ok'

    def regla_S2(self):  # S -> return X ;
        self.pila_aux.pop()
        x = self.pila_aux.pop()
        self.pila_aux.pop()
        s = self.pila_aux[-1]
        s.tipo = 'ok'
        s.ret = x.tipo

    def regla_X(self):  # X -> E
        e = self.pila_aux.pop()
        x = self.pila_aux[-1]
        x.tipo = e.tipo

    def regla_L(self):  # L -> E Q
        q = self.pila_aux.pop()
        e = self.pila_aux.pop()
        ll = self.pila_aux[-1]

        if q.tipo == 'vacio':
            ll.tipo = e.tipo
        else:
            ll.tipo = e.tipo + ' ' + q.tipo

    def regla_Q(self):  # Q-> , E Q1
        q1 = self.pila_aux.pop()
        e = self.pila_aux.pop()
        self.pila_aux.pop()
        q = self.pila_aux[-1]

        if q.tipo == 'vacio':
            q.tipo = e.tipo
        else:
            q.tipo = e.tipo + ' ' + q1.tipo

    def regla_H(self):  # H-> T
        t = self.pila_aux.pop()
        h = self.pila_aux[-1]
        h.tipo = t.tipo

    def regla_T1(self):  # T-> boolean
        self.pila_aux.pop()
        self.pila_aux[-1].tipo = 'logico'
        self.pila_aux[-1].ancho = 2

    def regla_T2(self):  # T-> string
        self.pila_aux.pop()
        self.pila_aux[-1].tipo = 'cadena'
        self.pila_aux[-1].ancho = 128

    def regla_T3(self):  # T-> number
        self.pila_aux.pop()
        self.pila_aux[-1].tipo = 'entero'
        self.pila_aux[-1].ancho = 2

    def regla_A1(self):  # A-> T ID
        id_ = self.pila_aux[-1]
        t = self.pila_aux[-2]
        self.gestor_ts.aniadir_variable_ts(id_.pos, t.tipo, t.ancho)

    def regla_A2(self):  # A-> T ID K
        k = self.pila_aux.pop()
        self.pila_aux.pop()
        t = self.pila_aux.pop()
        a = self.pila_aux[-1]

        if k.tipo == 'vacio':
            a.tipo = t.tipo
        else:
            a.tipo = t.tipo + ' ' + k.tipo

    def regla_K1(self):  # K -> , T ID
        id_ = self.pila_aux[-1]
        t = self.pila_aux[-2]
        self.gestor_ts.aniadir_variable_ts(id_.pos, t.tipo, t.ancho)

    def regla_K2(self):  # K -> , T ID K1
        k1 = self.pila_aux.pop()
        self.pila_aux.pop()
        t = self.pila_aux.pop()
        self.pila_aux.pop()
        k = self.pila_aux[-1]
        if k.tipo == 'vacio':
            k.tipo = t.tipo
        else:
            k.tipo = t.tipo + ' ' + k1.tipo

    def regla_lambda(self):
        self.pila_aux[-1].tipo = 'vacio'
