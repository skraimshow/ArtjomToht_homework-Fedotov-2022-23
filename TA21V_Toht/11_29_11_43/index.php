<!DOCTYPE html>
<html>
<head>
<meta harset="utf-8" />
<title></title>
</head>
<body>
<form method="post" action="bill.php" name="bill">
Client: <input type="text" name="clientName" /><br/>
Reg.nr: <input type="text" name="clientRegNum" /><br/>
Addres: <input type="text" name="clientAddr" /><br/>
<table border="0">
<tr>
<th>Product Name</th>
<th>Quantity</th>
<th>Price</th>
<th>Discount</th>
<th>Tax</th>
<th>Summ</th>
</tr>
<?php
$N=10;
for($i=1; $i<=$N; $i++){
echo '<tr>
<td><input type="text" name="prodName'.$i.'" size="40"  /></td>
<td><input type="text" name="prodNum'.$i.'" onchange="setSumm('.$i.')" size="3" value="0"/></td>
<td><input type="text" name="prodPrice'.$i.'" onchange="setSumm('.$i.')" size="6" value="0"/></td>
<td><input type="text" name="prodOff'.$i.'" onchange="setSumm('.$i.')" size="6" value="0"/></td>
<td><input type="text" name="prodTax'.$i.'" onchange="setSumm('.$i.')" size="3" value="0"/></td>
<td id="prodSumm'.$i.'"></td>
</tr>';
}
?>
</table>
<input type="submit" value="make bill" />
</form>
<script>
function setSumm(N){
	Qt=parseFloat(document.bill["prodNum"+N].value);
	Pr=parseFloat(document.bill["prodPrice"+N].value);
	Of=parseFloat(document.bill["prodOff"+N].value);
	Tx=parseInt(document.bill["prodTax"+N].value);
	Sm=Qt*Pr*(1-Of/100)*(1+Tx/100);
	Sm=Math.floor(Sm*100)/100;
	document.getElementById("prodSumm"+N).innerHTML=Sm;
}
</script>
</body>
</html>