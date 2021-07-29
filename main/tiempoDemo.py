import time

btc = 10
eth = 20
lit = 30
print ("Obteniendo consulta precion BTC (%s,%s), iteracion -> %s" % (btc,eth,lit))


def procedure():
   time.sleep(1)

# measure process time
t0 = time.process_time()
procedure()
print (time.process_time(), "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")

i = 0
while(i < 60 ):
    # measure wall time
    t1 = time.time()
    procedure()
    print (time.time() - t1, "seconds wall time")
    i = i + 1 

