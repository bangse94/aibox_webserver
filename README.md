# aibox_webserver
rockchip base aiobx(edge device) rtsp streaming webserver

##test 환경 1
|       |   Spec   |
|-------|----------|
|   OS  |    Mac   |
|  CPU  | M2(8core)|
|  Mem  |    8G    |

### test 결과
#### test '#1'
fps : origin
resize : True
|       |   Usage  |
|-------|----------|
|  CPU  |    57%   |
|  Mem  |   127M   |
#### test '#2'
fps : origin
resize : False
|       |   Usage  |
|-------|----------|
|  CPU  |   53.2%  |
|  Mem  |   127M   |
#### test '#3'
fps : origin // 5
resize : False
|       |   Usage  |
|-------|----------|
|  CPU  |   52.4%  |
|  Mem  |   126M   |
#### test '#4"
fps : origin // 10
resize : false
|       |   Usage  |
|-------|----------|
|  CPU  |   53.7%  |
|  Mem  |   120M   |
