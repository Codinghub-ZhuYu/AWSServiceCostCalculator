import pandas as pd

# environment varirables
ZHYProductcodeList = ['AmazonEC2','AmazonS3','AmazonRDS','AmazonES', 'AWSDirectConnect','AWSDataTransfer', 
    'AmazonElastiCache', 'AmazonCloudWatch','AWSLambda','AmazonCloudFront','AmazonEKS','AmazonWorkSpaces','OCBPremiumSupport']
BJSProductcodeList = ['AmazonEC2','AmazonS3','AmazonES','AmazonRDS','AWSLambda','AmazonApiGateway','AWSQueueService',
    'AmazonDynamoDB','AmazonElastiCache', 'AWSDirectConnect','AmazonSNS','AmazonECR','AmazonKinesis',
    'AmazonCloudWatch','AmazonMSK',  'AWSIoT','AWSCloudTrail', 'AmazonVPC', 'AmazonECR','AmazonEKS',
    'awskms','OCBPremiumSupport', 'AmazonCloudFront', 'AWSDataTransfer', 'AmazonECS','AmazonEFS',
    'ElasticMapReduce', 'IoTDeviceManagement',  'AmazonS3GlacierDeepArchive']
ZHYSOR = "Amazon Cloud Technology Services (Ningxia) Co., Ltd"
BJSSOR = "Amazon Web Services, Inc."
PayerRecordType = "PayerLineItem"
columneNames = ['RecordType', 'ProductCode','SellerOfRecord','CostBeforeTax']
CostBeforeTaxColumne = 'CostBeforeTax'

# cost explore
df = pd.read_csv (u"C:\ZhuYu\Workspace\Demos\PythonProject\Momenta_ecsv_5_2020.csv" )
# filter out the target column:
newdf = df[columneNames]
# get ZHY and BJS dataframe
ZHYdf = newdf[(newdf.SellerOfRecord == ZHYSOR) & (newdf.RecordType == PayerRecordType)]
BJSdf = newdf[(newdf.SellerOfRecord == BJSSOR) & (newdf.RecordType == PayerRecordType)]

print("ZHY serviceName, Cost***")
for i in ZHYProductcodeList:
    ZHYProdDF = ZHYdf[(ZHYdf.ProductCode == i )]
    ZHYCostDF = ZHYProdDF[[CostBeforeTaxColumne]].sum(axis=0)
    print( i , ',',ZHYCostDF[CostBeforeTaxColumne] )
print("BJS serviceName, Cost***")
for i in BJSProductcodeList:
    BJSProdDF = BJSdf[(BJSdf.ProductCode == i )]
    BJSCostDF = BJSProdDF[[CostBeforeTaxColumne]].sum(axis=0)
    print( i , ',',BJSCostDF[CostBeforeTaxColumne] )
