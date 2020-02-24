'''
Created on Jan 24, 2020

@author: mizuno
'''
import sympy as sp
import steepest_descent_method.Steepest_Descent_Method_lib as lib

# 今回の関数を定義
x0, x1, x2, a0 = sp.symbols('x0 x1 x2 a0')
f = 10*x1**2 +5*x1*x2 +10*(x2-3)**2 #関数f(x1,x2)
x0 = sp.Matrix([[10],[15]]) #初期値
sp.init_printing()

# コンストラクタの呼び出し
slib = lib.Steepest_Descent_Method(f, x0)
x = slib.getDescent()
print(x)