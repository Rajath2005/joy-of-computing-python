#Created on  Aug 28

import matplotlib.pyplot as plt
Estimate=[690, 682, 437, 615, 451, 527, 406, 338, 585, 521,
580, 526, 358, 451, 642, 393, 634, 417, 587, 391,
352, 600, 494, 572, 495, 593, 358, 602, 493, 339,
486, 580, 311, 365, 514, 328, 313, 319, 345, 391,
318, 534, 603, 530, 532, 453, 526, 567, 368, 400,
411, 497, 546, 512, 312, 421, 619, 532, 385, 390,
410, 383, 673, 515, 491, 329, 413, 564, 543, 501,
607, 483, 627, 688, 603
]

y=[]

Estimate.sort()
tv=int(0.1*len(Estimate))
Estimate=Estimate[tv:]
Estimate=Estimate[:len(Estimate)-tv]
for i in range(len(Estimate)):
    y.append(5)


plt.plot(Estimate,y,'ro')
plt.ylabel('some numbers')
plt.show()
