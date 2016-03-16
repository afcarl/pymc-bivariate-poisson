from math import factorial
import numpy as np
from bivpois import bivariate_poisson_like

def bivariate_poisson_like_classic(values, l_1, l_2, l_3):
    y_1 = values[0]
    y_2 = values[1]
    return -l_1-l_2-l_3+np.log(np.sum([(l_3**l/factorial(l)) * (l_1**(y_1-l)/factorial(y_1-l)) * (l_2**(y_2-l)/factorial(y_2-l)) for l in range(min(y_1,y_2)+1)]))

def test_likelihood():
    for n1 in range(6):
        for n2 in range(6):
            for l_1 in [.1,3.,90.,8.]:
                for l_2 in [.1,3.,90.,8.2]:
                    for l_3 in [.1,3.,90.,8.2]:
                        if not (abs(
                            bivariate_poisson_like_classic([n1,n2],l_1,l_2,l_3)
                            - bivariate_poisson_like([n1,n2],l_1,l_2,l_3)) < 1e-5):
                            print n1,n2,l_1,l_2,l_3
                            print bivariate_poisson_like_classic([n1,n2],l_1,l_2,l_3),bivariate_poisson_like([n1,n2],l_1,l_2,l_3)

if __name__ == '__main__':
    test_likelihood()
