---
title: Worked example
group: MM010: purchase order request
---
# Worked example: a real order

This is a real order from 2026, exactly as it was approved, with the society's three numbers and the treasurer's personal details removed. Pizza for a society's Annual General Meeting on 25 August 2026, ordered from Debonairs Rondebosch.

## The quote

Requested on 6 August, nineteen days before the event. Debonairs sent a quotation, number **D06082026 #2**, made out to the University of Cape Town, with the delivery date and time on it.

| Qty | Item | Unit price | Total |
| --- | --- | --- | --- |
| 50 | Large Margherita | R84.90 | R4 245.00 |
| 1 | Delivery | R100.00 | R100.00 |
| | Subtotal (excl. VAT) | | **R3 778.26** |
| | VAT at 15% | | R566.74 |
| | Total | | R4 345.00 |

Notice that the vendor's line items are VAT-inclusive (R84.90 is the shelf price) but the quote also shows the VAT-exclusive subtotal. The subtotal is the number the MM010 needs. Check: R4 345.00 divided by 1.15 is R3 778.26.

## The MM010

Submitted on 11 August. Here is every field as it was filled in.

| Field | Value |
| --- | --- |
| Requester name | the treasurer's full name |
| Tel. | the treasurer's mobile number |
| Department | Department of Student Affairs |
| Date | 11/08/2026 |
| Purchasing group | UCT Developer Society |
| Vendor name | T/A Debonairs Pizza Rondebosch |
| Vendor number | 206415 |
| Item details | Pizza for our Annual General Meeting event scheduled for the 25th of August |
| Qty | 1 |
| Unit net amount (excl. VAT) | 3778.26 |
| Currency | ZAR |
| Total ZAR amount (excl. VAT) | 3778.26 |
| Fund number | the society's fund number |
| Cost centre | the society's cost centre |
| GL account number | the society's GL number |
| TOTAL | 3778.26 |
| Vendor selection procedure followed | YES |
| Conflict of interest | NO |
| Fund holder block | left blank |

Three things to learn from it.

**One row, not two.** The pizzas and the delivery fee were combined into one line for the whole order at the VAT-exclusive subtotal, quantity 1. That is allowed and it removes a place to make an arithmetic mistake.

**The description could have been better.** It says what and when, which is what got it approved, but it does not include the quote number, and it is well over 40 characters. `Q#D06082026 #2 pizza for AGM 25 Aug` would have been tighter and would let Treasury match the form to the quote without opening the attachment.

**Vendor name as registered.** The register lists this vendor as "Dokrek Beleggings T/A Debonairs Pizza Rondebosch". The form used the trading-name part and was accepted, but the full registered name is the safer choice.

## What came back

The fund holder signed it, and Student Treasury created purchase order **2106858** and emailed it to the treasurer, who forwarded it to Debonairs. On the day of the AGM, Debonairs delivered and issued a VAT invoice with the same quote number and the PO number printed on it, for R4 345.00 including VAT. The treasurer sent that invoice to Treasury with a note confirming delivery, and UCT paid Debonairs. The society's fund was reduced by the VAT-inclusive amount.

## The timeline

| Date | Event |
| --- | --- |
| 6 Aug | Quote requested and received |
| 11 Aug | MM010 sent to the fund holder mailbox |
| by 18 Aug | PO created and emailed back (within a week on every 2026 order from this society) |
| 25 Aug | Delivery, event, invoice issued |
| after 25 Aug | Invoice and delivery confirmation sent to Treasury; UCT Creditors pays the vendor |

## Two more orders from the same society, briefly

**Opening event, March 2026.** Quote on 23 February, MM010 on 26 February, PO 2080364 created on 2 March, delivery 7 March. Four rows, one per kind of pizza plus delivery, total R544.70 excluding VAT. The PO showed R626.40, which is that amount with VAT added.

**Industry event, May 2026.** Quote and MM010 both on 7 May, PO 2091717 on 12 May, event 16 May. Two rows, "pizza" and "cool drinks", total R5 111.30 excluding VAT.

Both of these used the old Department and Purchasing group values described on the field guide. They were accepted at the time. They would not be today.
