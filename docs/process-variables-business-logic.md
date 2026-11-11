# Process Variables, Gateways and Business Logic

## 1. Introduction

This document explains the process variables, gateways and business rules that are needed for Case 2.

The main aim is to support customers when they place orders from different producers, make payments and complete checkout. It also covers how the system handles stock availability and producer payments.

These details will be used as a starting point for the Camunda implementation and will be checked against the group's BPMN diagrams.

## 2. Process Variables

Process variables are used to store information while the order process is running. The following variables are suggested for Case 2.

| Variable | Data Type | Description |
|---|---|---|
| orderId | String | Stores the order reference. |
| customerId | String | Identifies the customer. |
| productId | String | Identifies the selected product. |
| productName | String | Stores the product name. |
| requestedQuantity | Integer | Stores how many items the customer wants. |
| availableStock | Integer | Stores the current stock quantity. |
| unitPrice | Number | Stores the price of one product. |
| orderTotal | Number | Stores the total order amount. |
| stockAvailable | Boolean | Shows whether there is enough stock. |
| paymentStatus | String | Records whether the payment was successful or declined. |
| paymentRetryCount | Integer | Keeps track of payment attempts. |
| commissionRate | Number | Stores the marketplace commission rate. |
| commissionAmount | Number | Stores the commission amount. |
| producerAmount | Number | Stores the amount due to the producer. |

The final variable names and data types will be agreed with the group when the Camunda process is developed.

## 3. Gateways

Gateways help the process decide what should happen next, depending on the information received.

### 3.1 Stock Availability Gateway

This gateway checks whether enough stock is available for the customer's order.

- If there is enough stock, the customer can continue to checkout.
- If there is not enough stock, the customer is informed and can change the requested quantity.

### 3.2 Payment Result Gateway

After the customer makes a payment, the system checks the result from the payment service.

- If the payment is successful, the order can be confirmed and the stock can be updated.
- If the payment is declined, the customer is informed and can try again.
- If the payment service is unavailable, the system should follow the agreed retry or error-handling process.

### 3.3 Payment Retry Gateway

This gateway checks whether the customer can make another payment attempt.

- If another attempt is allowed, the payment process starts again.
- If no more attempts are allowed, the process stops and the customer is informed.

## 4. Business Logic

The following business rules describe how the system should handle orders and payments.

### 4.1 Checking Stock

The system compares the quantity requested by the customer with the available stock.

If the customer requests more items than are available, the system should not confirm the order. The customer should be given the option to change the quantity.

### 4.2 Confirming an Order

An order should only be confirmed when the payment has been successful. If the payment is declined, the order must not be marked as paid.

### 4.3 Updating Stock

Once payment is successful, the system should reduce the available stock by the quantity ordered.

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

A customer may buy products from more than one producer in the same order. The system should split the overall order into separate order elements for the relevant producers.

This allows each producer to see and manage their own part of the order.

### 4.6 Producer Preparation Time

Producers need enough time to prepare their products. The system should provide incoming order information with at least 48 hours' notice.

### 4.7 Weekly Payments to Producers

Producer payments should be settled weekly. The system should also keep a clear record of transactions so that producers can use the information for their accounts and tax reporting.

## 5. Camunda Implementation

These variables and business rules will be used when setting up the Camunda process.

The gateways will help the process choose the correct path when checking stock and handling payment results.

The business logic will be used for stock checking, updating inventory and calculating the 5% marketplace commission.

The implementation will need to match the operational BPMN diagrams and the user tasks and forms being developed by the other group members.

## 6. Notes

This document is an initial plan for the process variables, gateways and business logic. Some details may need to change once the group has agreed on the final BPMN diagrams and started implementing the process in Camunda.

## 7. Checking the BPMN Diagram Against the Business Logic

After looking at our group's BPMN diagram, I compared it with the process variables and business rules in this document. Most of the main steps, such as placing an order, processing payment and sending messages to customers and producers, are already included in the diagram.

However, there are still a few details that need to be checked with the group before we start the Camunda implementation.

| Requirement | What is shown in the BPMN diagram | What still needs to be checked |
|---|---|---|
| Order placement | The customer can place an order. | Make sure the order details are stored correctly. |
| Stock availability | There is a gateway to check whether an order is possible. | Check that it compares the requested quantity with the available stock. |
| Payment processing | The marketplace processes the payment and checks whether it is approved. | Make sure the payment result is stored correctly. |
| Payment retry | The customer can follow a retry path. | Agree on how many payment attempts should be allowed. |
| Order confirmation | The marketplace sends messages to the customer and producer. | Make sure confirmation is only sent after successful payment. |
| Stock update | This is not clearly shown in the current diagram. | Decide where the stock should be reduced after payment. |
| Marketplace commission | This is not clearly shown in the current diagram. | Include the 5% commission calculation. |
| Producer payments | The producer receives and fulfils the order. | Agree on how producer payments and transaction records will be managed. |
| Multiple producers | The marketplace communicates with producers. | Check how orders will be separated when customers buy from different producers. |
| 48-hour preparation time | This is not clearly shown in the current diagram. | Decide how the system will make sure producers have enough preparation time. |

### 7.1 Things to Discuss Before Implementation

Before starting the Camunda implementation, there are a few things that the group still needs to agree on:

- How the system will check available stock and update it after an order.
- How many times a customer can retry a declined payment.
- What should happen if the payment service is unavailable.
- How the marketplace will calculate its 5% commission.
- How producer payments and transaction history will be recorded.
- How the system will handle the minimum 48-hour preparation time.

These details will help us make sure that the process variables and business rules work correctly with the final BPMN diagrams.

### 7.2 Conclusion

This document is an initial guide for the process variables, gateways and business logic needed for Case 2. Some details may change as the group discusses the design and starts working on the Camunda implementation. I will update the document when the final decisions have been agreed with the group.
