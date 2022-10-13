import sys
import apt_pkg
import apt


conta = 0


apt_pkg.init()

apt_pkg.config.set("Dir::Cache::pkgcache","")


try:
    cache = apt_pkg.Cache(apt.progress.base.OpProgress())
except SystemError as e:
    sys.stderr.write("Error: Opening the cache (%s)" % e)
    sys.exit(-1)

depcache = apt_pkg.DepCache(cache)

for pkg in depcache.is_upgradable:
    if pkg == False:
        continue
    conta = conta + 1

print(conta)