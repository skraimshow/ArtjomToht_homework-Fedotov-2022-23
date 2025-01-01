<?php
require "TCPDF/tcpdf.php";
$bill = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$bill->setPrintHeader(false);
$bill->setPrintFooter(false);
$bill->SetFont('dejavusans', '', 12);
$bill->AddPage();
$bill->setXY(20,30);
$bill->Cell(0,0,'Client name: '.$_POST['clientName'],0,0,'L',0,'',0);
$bill->setXY(20,40);
$bill->Cell(0,0,'Reg. num.: '.$_POST['clientRegNum'],0,0,'L',0,'',0);
$bill->setXY(20,50);
$bill->Cell(0,0,'Address: '.$_POST['clientAddr'],0,0,'L',0,'',0);

$bill->Output('example_002.pdf', 'I');
?>