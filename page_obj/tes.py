
import  subprocess




cmd = 'cd .. &start grpcurl.exe &grpcurl -plaintext -d "{\\"orderNo\\": \\"BPA0212011013990\\", \\"fininstId\\": 11, \\"reqId\\": \\"0176658bded801f18a7286c176467782\\"}" grpc-cango-fininst-gw.cango.local:8080 org.cango.fininst.gw.api.FininstGwService.preApplyQuery'
res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,stderr=subprocess.STDOUT)
aa = res.stdout.read().decode("utf8")
print(aa)