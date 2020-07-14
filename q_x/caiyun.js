let body = JSON.parse($response.body)
body.result.xy_vip_expire = 0
body.result.is_vip = true
body.result.vip_expired_at = 0
body.result.svip_expired_at = 4070883661.2019770145
body.result.wt.vip.enable = true
body.result.wt.vip.svip_expired_at = 4070883661.2019770145
$done({ body: JSON.stringify(body) })
