import pandas as pd
import csv

# environment varirables
ZHYProductcodeList = ['AmazonEC2','AmazonS3','AmazonRDS','AmazonES', 'AWSDirectConnect','AWSDataTransfer', 
    'AmazonElastiCache', 'AmazonCloudWatch','AWSLambda','AmazonCloudFront','AmazonEKS','AmazonWorkSpaces','OCBPremiumSupport']
BJSProductcodeList = ['AmazonEC2','AmazonS3','AmazonES','AmazonRDS','AWSDataTransfer','AWSLambda','AmazonApiGateway','AWSQueueService',
    'AmazonDynamoDB','AmazonElastiCache', 'AWSDirectConnect','AmazonSNS','ElasticMapReduce','AmazonKinesis',
    'AmazonCloudWatch','AmazonMSK', 'AWSIoT','AmazonS3GlacierDeepArchive',
    'AWSCloudTrail', 'AmazonVPC', 'AmazonECR','AmazonEKS',
    'awskms','OCBPremiumSupport', 'AmazonCloudFront', 'AmazonECS','AmazonEFS',
    'IoTDeviceManagement']
ZHYSOR = "Amazon Cloud Technology Services (Ningxia) Co., Ltd"
BJSSOR = "Amazon Web Services, Inc."
PayerRecordType = "PayerLineItem"
columneNames = ['RecordType', 'ProductCode','SellerOfRecord','CostBeforeTax']
CostBeforeTaxColumne = 'CostBeforeTax'

# cost explore
df = pd.read_csv (u"C:\ZhuYu\Workspace\Demos\PythonProject\ecsv_5_2020.csv" )
# filter out the target column:
newdf = df[columneNames]
# get ZHY and BJS dataframe
ZHYdf = newdf[(newdf.SellerOfRecord == ZHYSOR) & (newdf.RecordType == PayerRecordType)]
BJSdf = newdf[(newdf.SellerOfRecord == BJSSOR) & (newdf.RecordType == PayerRecordType)]

with open("./PythonProject/result.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    csv_head = ["ServiceName", "Cost"] 
    writer.writerow(csv_head)
    writer.writerow(["ZHY ******"])
    for i in ZHYProductcodeList:
        ZHYProdDF = ZHYdf[(ZHYdf.ProductCode == i )]
        ZHYCostDF = ZHYProdDF[[CostBeforeTaxColumne]].sum(axis=0)
        writer.writerow([i,ZHYCostDF[CostBeforeTaxColumne]])
    writer.writerow(["BJS ******"])
    for i in BJSProductcodeList:
        BJSProdDF = BJSdf[(BJSdf.ProductCode == i )]
        BJSCostDF = BJSProdDF[[CostBeforeTaxColumne]].sum(axis=0)
        writer.writerow([i, BJSCostDF[CostBeforeTaxColumne]])
       
