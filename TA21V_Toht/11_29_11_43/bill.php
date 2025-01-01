<?php
require "TCPDF/tcpdf.php";
$bill = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$bill->setPrintHeader(false);
$bill->setPrintFooter(false);
$bill->SetFont('dejavusans', '',12);
$bill->AddPage();
// кому
$bill->setXY(20,50);
$bill->Cell(0,0,'Client name: '.$_POST['clientName'],0,0,'L',0,'',0);
$bill->setXY(20,60);
$bill->Cell(0,0,'Reg. num.: '.$_POST['clientRegNum'],0,0,'L',0,'',0);
$bill->setXY(20,70);
$bill->Cell(0,0,'Address: '.$_POST['clientAddr'],0,0,'L',0,'',0);
// от кого
$bill->setXY(120,10);
$bill->Cell(0,0,'Sender name: Loly-Poly company ',0,0,'L',0,'',0);
$bill->setXY(120,20);
$bill->Cell(0,0,'Address: 111 Lake Dr',0,0,'L',0,'',0);
$bill->setXY(120,30);
$bill->Cell(0,0,'Tallinn. EE 11111',0,0,'L',0,'',0);
// причина
$bill->setXY(120,50);
$bill->Cell(0,0,'Сause:',0,0,'L',0,'',0);
$bill->setXY(120,60);
$bill->Cell(0,0,'Lorem Ipsum is simply dummy text',0,0,'L',0,'',0);
$bill->setXY(120,70);
$bill->Cell(0,0,'Lorem Ipsum has been the industry',0,0,'L',0,'',0);
// лого
$bill->Image('santa_mark.jpg', 20, 5, 50, 0, 'JPG', 'http://www.tcpdf.org', '', false, 150, '', false, false, 0, false, false, false);

$bill->Output('example_002.pdf', 'I');
?>