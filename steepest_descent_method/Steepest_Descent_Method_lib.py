'''
Created on Jan 24, 2020

@author: mizuno
'''
import sympy as sp

class Steepest_Descent_Method:

    def __init__(self, f, x0):
        self._f = f #関数f
        self._x0 = sp.symbols('x0')
        x1, x2 = sp.symbols('x1 x2') #今回は2変数(x1, x2)
        self._x0 = x0
        self._dfx1 = sp.diff(f, x1) #x1での偏微分
        self._dfx2 = sp.diff(f, x2) #x2での偏微分
        self._df = sp.Matrix([[self._dfx1], [self._dfx2]])
        print(self._f)
        print(self._dfx1)
        print(self._dfx2)
        print(self._df)

    def getDescent(self):
        x1, x2, a0 = sp.symbols('x1 x2 a0') #今回は2変数(x1, x2)
        for i in range(3): #今回は3回ループ
            print(str(i)+'回目')
            dfx0 = sp.Matrix([[self._df[0].subs([(x1, self._x0[0]), (x2, self._x0[1])])],[self._df[1].subs([(x1, self._x0[0]), (x2, self._x0[1])])]])
            print(dfx0)
            #x0の更新
            self._x0 = self._x0 - a0 * dfx0
            print(self._x0)
            #更新したx0の値をfに代入(a0の式)
            fa0 = self._f.subs([(x1, self._x0[0]),(x2, self._x0[1])])
            print(fa0)
            #fa0が最小となるa0を求める
            #今回は２次関数なので、極小値となるa0を求める
            # solveはlistで返すので注意
            a0_val = sp.solve(sp.diff(fa0, a0))
            a0_val = float(a0_val[0])
            print(a0_val)
            self._x0 = self._x0.subs(a0,a0_val)
            print(self._x0)
        return self._x0