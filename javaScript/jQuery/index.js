$("button").text("Click");
text=""
$(".input").keypress((e)=>{
    console.log(e.key);
    text=text+(e.key)
    $("textarea").text(text)
})
$(".reset").click(()=>{
    $("textarea").text("")
})

