function main(splash, args)
    local treat = require("treat")
    local json = require("json")
    local response = splash:http_post {
        "http://httpbin.org/post",
        body = json.encode({ name = "Germey" }),
        headers = { ["content-type"] = "application/json" }
    }
    -- 获取网页加载的过程描述
    local har = splash:har()
    return {
        har = har,
        html = treat.as_string(response.body),
        url = response.url,
        status = response.status
    }
end



--[[
    元素选择
--]]
function main(splash)
    splash:go("https://www.baidu.com/")
    -- css选择器
    input = splash:select("#kw")
    input:send_text('Splash')
    splash:wait(3)
    return splash:png()
end

function main(splash)
    local treat = require('treat')
    assert(splash:go("http://quotes.toscrape.com/"))
    -- 选择所有
    local texts = splash:select_all('.quote .text')
    local results = {}
    for index, text in ipairs(texts) do
        results[index] = text.node.innerHTML
    end
    return treat.as_array(results)
end


--[[
    模拟点击
-- ]]

function main(splash)
    splash:go("https://www.baidu.com/")
    input = splash:select("#kw")
    input:send_text('Splash')
    submit = splash:select('#su')
    submit:mouse_click()
    splash:wait(3)
    return splash:png()
end
