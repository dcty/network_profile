let body = JSON.parse($response.body)
let newsList = body.newslist
if (newsList && newsList.length > 0){
    let index = newsList.length
    while(index--){
        let news = newsList[index]
        if ("aid" in news){
            newsList.splice(index,1)
        }
    }
}

$done({ body: JSON.stringify(body) })
