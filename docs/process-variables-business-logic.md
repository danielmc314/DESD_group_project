# Process Variables, Gateways and Business Logic

## 1. Introduction

This document describes the process variables, gateways and business rules required for Case 2.

The main aim is to support customers when they place orders from different producers, make payments and complete the checkout process. It also explains how the system handles stock availability and payments to producers.

This information will be used as a starting point for the Camunda implementation and will be checked against the group's BPMN diagrams.

## 2. Process Variables

Process variables store information while an order process is running. The following variables are suggested for Case 2.

| Variable | Data Type | Description |
|---|---|---|
| orderId | String | Stores the order reference. |
| customerId | String | Identifies the customer. |
| productId | String | Identifies the selected product. |
| productName | String | Stores the product name. |
| requestedQuantity | Integer | Stores the quantity requested by the customer. |
| availableStock | Integer | Stores the current stock quantity. |
| unitPrice | Number | Stores the price of one product. |
| orderTotal | Number | Stores the total order amount. |
| stockAvailable | Boolean | Shows whether enough stock is available. |
| paymentStatus | String | Records whether the payment was successful or declined. |
| paymentRetryCount | Integer | Keeps track of the number of payment attempts. |
| commissionRate | Number | Stores the marketplace commission rate. |
| commissionAmount | Number | Stores the commission amount. |
| producerAmount | Number | Stores the amount due to the producer. |
| itemAvailability | List | Stores the stock availability result for each order item. |
| unavailableItems | List | Stores products that are unavailable or have insufficient stock. |
| orderValidity | Boolean | Shows whether the order is valid based on the validation results. |
| dateAvailability | List | Stores the date validation result for each order item. |
| dateValid | Boolean | Shows whether a product meets the requested fulfilment date. |
|requestedFulfilmentDate | date | shows customers wanted delivery date |
|collectionType | string | shows customers preferred means of delivery |

The date check also uses `customerOrder.requestedFulfilmentDate` and `product.bestBeforeDate`. These values are compared to check whether the requested fulfilment date is suitable for the product.

The final variable names and data types will be agreed with the group during the Camunda implementation.

## 3. Gateways

Gateways allow the process to make decisions and choose the correct path based on the information received.

### 3.1 Stock Availability Gateway

This gateway checks whether enough stock is available for the customer's order.

- If enough stock is available, the customer can continue to checkout.
- If there is not enough stock, the customer is informed and can change the requested quantity.

### 3.2 Payment Result Gateway

After the customer makes a payment, the system checks the result returned by the payment service.

- If the payment is successful, the order can be confirmed and the stock can be updated.
- If the payment is declined, the customer is informed and may try again.
- If the payment service is unavailable, the system should follow the retry or error-handling process agreed by the group.

### 3.3 Payment Retry Gateway

This gateway checks whether the customer is allowed to make another payment attempt.

- If another attempt is allowed, the payment process starts again.
- If no more attempts are allowed, the process stops and the customer is informed.

## 4. Business Logic

The following business rules explain how the system should handle orders and payments.

### 4.1 Checking Stock

The system compares the quantity requested by the customer with the available stock.

If the customer requests more items than are available, the system should not confirm the order. Instead, the customer should be given the option to change the requested quantity.

### 4.2 Confirming an Order

An order should only be confirmed after the payment has been successful. If the payment is declined, the order must not be marked as paid.

### 4.3 Updating Stock

After a successful payment, the system should reduce the available stock by the quantity ordered.

For example, if there are 10 apples available and the customer buys 3, the remaining stock should be 7.

### 4.4 Calculating the Marketplace Commission

The marketplace takes a 5% commission from the relevant order amount.

The calculation is:

- Commission = Order Total × 5%
- Producer Amount = Order Total − Commission

For example, if the order total is £100:

- Marketplace commission = £5
- Producer amount = £95

This example does not include any additional fees.

### 4.5 Handling Orders from Different Producers

A customer may buy products from more than one producer in the same order. The system should divide the overall order into separate parts for the relevant producers.

This allows each producer to view and manage their own part of the order.

### 4.6 Producer Preparation Time

Producers need enough time to prepare their products. The system should provide producers with incoming order information at least 48 hours in advance.

### 4.7 Weekly Payments to Producers

Payments to producers should be settled weekly. The system should also keep clear transaction records so that producers can use the information for their accounts and tax reporting.

## 5. Camunda Implementation

The process variables and business rules described in this document will be used when setting up the Camunda process.

The gateways will help the process choose the correct path when checking stock availability and handling payment results.

The business logic will be used for stock checking, inventory updates and calculating the 5% marketplace commission.

The implementation will need to match the operational BPMN diagrams and the user tasks and forms being developed by the other group members.

## 6. Notes

This document is an initial plan for the process variables, gateways and business logic. Some details may need to change once the group has agreed on the final BPMN diagrams and started implementing the process in Camunda.

## 7. Checking the BPMN Diagram Against the Business Logic

After reviewing the group's BPMN diagram, I compared it with the process variables and business rules in this document. Most of the main steps, such as placing an order, processing payments and sending messages to customers and producers, are already included in the diagram.

However, some details still need to be checked with the group before the Camunda implementation begins.

| Requirement | What is shown in the BPMN diagram | What still needs to be checked |
|---|---|---|
| Order placement | The customer can place an order. | Check that the order details are stored correctly. |
| Stock availability | There is a gateway to check whether an order can proceed. | Check that it compares the requested quantity with the available stock. |
| Payment processing | The marketplace processes the payment and checks whether it is approved. | Check that the payment result is stored correctly. |
| Payment retry | The customer can follow a retry path. | Agree on the number of payment attempts allowed. |
| Order confirmation | The marketplace sends messages to the customer and producer. | Make sure confirmation is only sent after successful payment. |
| Stock update | This is not clearly shown in the current diagram. | Decide where the stock should be reduced after payment. |
| Marketplace commission | This is not clearly shown in the current diagram. | Include the 5% commission calculation. |
| Producer payments | The producer receives and fulfils the order. | Agree on how producer payments and transaction records will be managed. |
| Multiple producers | The marketplace communicates with producers. | Check how orders will be separated when customers buy from different producers. |
| 48-hour preparation time | This is not clearly shown in the current diagram. | Decide how the system will make sure producers have enough preparation time. |

## 8. Camunda Implementation

I have started looking at how process variables and business rules can be used in Camunda. So far, I have worked on stock availability checking and order validation.

### 8.1 Stock Availability

I used a Script Task called `check product stock and availability` to check whether the products in a customer's order are available.

The script uses `itemAvailability` to store the result for each order item. It checks whether the product exists in the inventory, is active and has enough stock for the quantity requested by the customer.

It also checks that the requested quantity is greater than zero.

### 8.2 Order Validation

After the stock check, the process moves on to order validation.

I used another Script Task called `record order validation results`. Its result variable is `orderValidity`.

The FEEL expression checks the `unavailableItems` list. If the list is empty, `orderValidity` is set to true, which means the order is valid. If the list contains unavailable items, the result is false.

### 8.3 Order Validity Gateway

The gateway named `is order valid` decides what happens next.

I used the condition `orderValidity = true` for the yes path. If the order is valid, the process continues and sends the order summary. If it is not valid, the customer is informed and can amend the order.

I will continue checking these steps against the group's BPMN diagram as the Camunda implementation develops.

### 8.4 Payment Result and Retry Logic

After the customer makes a payment, the system checks the result returned by the payment service. The `paymentStatus` variable is used to store the result.

- If the payment is successful, the status is set to `"Success"` and the order can move on to confirmation.
- If the payment is declined, the status is set to `"Declined"` and the customer is informed.
- The payment result gateway checks the status and decides which path the process should follow.

The system also uses `paymentRetryCount` to keep track of the number of payment attempts.

If the customer is allowed to try again, the payment process can start again. If no more attempts are allowed, the order should be cancelled or handled using the error process agreed by the group.

The customer can retry a declined payment up to 3 times. This means there can be one initial payment attempt and up to 3 additional attempts. If all attempts fail, the order should be cancelled or handled through the agreed error process.

### 8.5 Commission Calculation Logic

The marketplace keeps 5% of the relevant order amount as commission. The remaining amount goes to the producer.

The following variables are used for this calculation:

- `orderTotal` stores the total order amount.
- `commissionRate` stores the commission rate (0.05).
- `commissionAmount` stores the amount kept by the marketplace.
- `producerAmount` stores the amount the producer receives.

The calculation is:

- `commissionAmount = orderTotal * commissionRate`
- `producerAmount = orderTotal - commissionAmount`

For example, if the order total is £100, the marketplace keeps £5 and the producer receives £95.

The 5% commission will be calculated for each producer's part of the order. It will also be calculated on the overall order total. The overall commission should match the sum of the commissions calculated for each producer. This will help keep the payment amounts clear and make the totals easier to check.

## 9. Conclusion

This document provides an overview of the process variables, gateways and business logic required for Case 2. It also describes the work completed so far in Camunda, including stock availability checking and order validation.

Further work is still needed to check the payment retry logic and commission calculations against the group's BPMN diagrams. The document will be updated as the implementation develops and the group agrees on the final decisions.
