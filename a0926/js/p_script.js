$(function(){

  $("#search_btn").click(function(){
    alert("검색 버튼 클릭");

    let s_url = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=Hsz86HytRSW99U2%2Bt3MCW3D2NHpZqiV7JRmD6AA0Y745SzCdK4UqRmRAYGsurVkJAGDr1OGLuVnY2NoujU3Q4A%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    s_url += searchWord;

    $.ajax({
      url : s_url,
      type : "get", 
      data : "", 
      dataType : "json",
  
      success : function(data){
        alert("성공");
        console.log(data);

        let dataList = data.response.body.items.item;

        let s_data = "";

        for(var i = 0; i < 10; i++){
  
          s_data += `<tr id='${dataList[i].galContentId}'>`;
          s_data += `<td>${dataList[i].galContentId}</td>`;
          s_data += `<td>${dataList[i].galTitle}</td>`;
          s_data += `<td>${dataList[i].galPhotographer}</td>`;
          s_data += `<td>${dataList[i].galCreatedtime}</td>`;
          s_data += `<td><img src='${dataList[i].galWebImageUrl}'></td>`;
          s_data += `</tr>`;
        }
        $("#tbody").html(s_data);



      },
      error : function(){
        alert("실패");
      }
    }); // ajax



  });  // #search_btn
}); // jquery