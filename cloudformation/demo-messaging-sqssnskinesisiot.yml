---
AWSTemplateFormatVersion: '2010-09-09'
Description: >
  Author: Alick Li
  Purpose: Class Demostration
  Info: 
  This yaml template is used to support messaging demo
Parameters:
Resources:
  LambdaKinesisToSQSRole:
    Type: "AWS::IAM::Role"
    Properties:
      RoleName: LambdaKinesisToSQSRole
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - "sts:AssumeRole"
      Path: /
      Policies:
        - PolicyName: LambdaKinesisToSQSPolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - "sns:*"
                  - "sqs:*"
                  - "kinesis:*"
                  - "cloudwatch:*"
                  - "logs:*"
                Resource: "*"
  microservicesDrawQueueFIFO:
    Properties:
      QueueName: microservices_drawqueue.fifo
      FifoQueue: true
      ContentBasedDeduplication: true
    Type: "AWS::SQS::Queue"
  microservicesDrawQueueStandard1:
    Properties:
      QueueName: microservices_drawqueue_1
    Type: "AWS::SQS::Queue"
  microservicesDrawQueueStandard2:
    Properties:
      QueueName: microservices_drawqueue_2
    Type: "AWS::SQS::Queue"
  microservicesDrawQueueStandard3:
    Properties:
      QueueName: microservices_drawqueue_3
    Type: "AWS::SQS::Queue"
  CIPMessageDraw:
    Type: "AWS::Cognito::IdentityPool"
    Properties:
      IdentityPoolName: microservices_Messaging
      AllowUnauthenticatedIdentities: true
  microservicesDrawTopic:
    Type: "AWS::SNS::Topic"
    Properties:
      Subscription:
        - Endpoint: !GetAtt
            - microservicesDrawQueueStandard1
            - Arn
          Protocol: sqs
        - Endpoint: !GetAtt
            - microservicesDrawQueueStandard2
            - Arn
          Protocol: sqs
        - Endpoint: !GetAtt
            - microservicesDrawQueueStandard3
            - Arn
          Protocol: sqs
      TopicName: microservicesMessageDuplicator
  KinesisStreamDrawingData:
    Type: "AWS::Kinesis::Stream"
    Properties:
      Name: microservicesDrawingData
      RetentionPeriodHours: 24
      ShardCount: 1
  CognitoRolesAttachment:
    Type: "AWS::Cognito::IdentityPoolRoleAttachment"
    Properties:
      IdentityPoolId: !Ref CIPMessageDraw
      Roles:
        unauthenticated: !GetAtt
          - CognitoIAMUnauthenticatedRole
          - Arn
        authenticated: !GetAtt
          - CognitoIAMAuthenticatedRole
          - Arn
  CognitoIAMUnauthenticatedRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Federated: cognito-identity.amazonaws.com
            Action: "sts:AssumeRoleWithWebIdentity"
            Condition:
              StringEquals:
                "cognito-identity.amazonaws.com:aud": !Ref CIPMessageDraw
              "ForAnyValue:StringLike":
                "cognito-identity.amazonaws.com:amr": unauthenticated
      Path: /
      Policies:
        - PolicyName: StandardCognito
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - "mobileanalytics:PutEvents"
                  - "cognito-sync:*"
                Resource:
                  - "*"
        - PolicyName: SNSPolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - "sns:*"
                Resource:
                  - !Ref microservicesDrawTopic
        - PolicyName: KinesisPolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - "kinesis:PutRecord"
                  - "kinesis:PutRecords"
                Resource:
                  - !GetAtt
                    - KinesisStreamDrawingData
                    - Arn
        - PolicyName: SQSPolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - "sqs:*"
                Resource:
                  - !GetAtt
                    - microservicesDrawQueueStandard1
                    - Arn
                  - !GetAtt
                    - microservicesDrawQueueStandard2
                    - Arn
                  - !GetAtt
                    - microservicesDrawQueueStandard3
                    - Arn
                  - !GetAtt
                    - microservicesDrawQueueFIFO
                    - Arn
        - PolicyName: IoTPolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - "iot:Connect"
                Resource:
                  - "*"
              - Effect: Allow
                Action:
                  - "iot:Publish"
                  - "iot:Receive"
                Resource:
                  - "arn:aws:iot:*:*:topic/microservices/drawingdemo"
              - Effect: Allow
                Action:
                  - "iot:Subscribe"
                Resource:
                  - "arn:aws:iot:*:*:topicfilter/microservices/drawingdemo"
  CognitoIAMAuthenticatedRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Federated: cognito-identity.amazonaws.com
            Action: "sts:AssumeRoleWithWebIdentity"
            Condition:
              StringEquals:
                "cognito-identity.amazonaws.com:aud": !Ref CIPMessageDraw
              "ForAnyValue:StringLike":
                "cognito-identity.amazonaws.com:amr": authenticated
      Path: /
      Policies:
        - PolicyName: StandardCognito
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - "mobileanalytics:PutEvents"
                  - "cognito-sync:*"
                Resource:
                  - "*"
  SQSPolicyStandard1:
    Type: "AWS::SQS::QueuePolicy"
    Properties:
      PolicyDocument:
        Version: 2012-10-17
        Id: AllowAll
        Statement:
          - Sid: "1"
            Effect: Allow
            Principal: "*"
            Action:
              - "sqs:SendMessage"
              - "sqs:ReceiveMessage"
            Resource: !GetAtt microservicesDrawQueueStandard1.Arn
            Condition:
              ArnEquals:
                aws:SourceArn: !Ref microservicesDrawTopic
      Queues:
        - !Ref microservicesDrawQueueStandard1
  SQSPolicyStandard2:
    Type: "AWS::SQS::QueuePolicy"
    Properties:
      PolicyDocument:
        Version: 2012-10-17
        Id: AllowAll
        Statement:
          - Sid: "1"
            Effect: Allow
            Principal: "*"
            Action:
              - "sqs:SendMessage"
              - "sqs:ReceiveMessage"
            Resource: !GetAtt microservicesDrawQueueStandard2.Arn
            Condition:
              ArnEquals:
                aws:SourceArn: !Ref microservicesDrawTopic
      Queues:
        - !Ref microservicesDrawQueueStandard2
  SQSPolicyStandard3:
    Type: "AWS::SQS::QueuePolicy"
    Properties:
      PolicyDocument:
        Version: 2012-10-17
        Id: AllowAll
        Statement:
          - Sid: "1"
            Effect: Allow
            Principal: "*"
            Action:
              - "sqs:SendMessage"
              - "sqs:ReceiveMessage"
            Resource: !GetAtt microservicesDrawQueueStandard3.Arn
            Condition:
              ArnEquals:
                aws:SourceArn: !Ref microservicesDrawTopic
      Queues:
        - !Ref microservicesDrawQueueStandard3
  SQSPolicyFIFO:
    Type: "AWS::SQS::QueuePolicy"
    Properties:
      PolicyDocument:
        Version: 2012-10-17
        Id: AllowAll
        Statement:
          - Sid: "1"
            Effect: Allow
            Principal: "*"
            Action:
              - "sqs:SendMessage"
              - "sqs:ReceiveMessage"
            Resource: !GetAtt microservicesDrawQueueFIFO.Arn
            Condition:
              ArnEquals:
                aws:SourceArn: !Ref microservicesDrawTopic
      Queues:
        - !Ref microservicesDrawQueueFIFO

Outputs:
  QueueUrl1:
    Description: SQS.Standard.QueueUrl
    Value: !Ref microservicesDrawQueueStandard1
  QueueUrl2:
    Description: SQS.Secondary.QueueUrl
    Value: !Ref microservicesDrawQueueStandard2
  QueueUrl3:
    Description: SQS.Tertiary.QueueUrl
    Value: !Ref microservicesDrawQueueStandard3
  FIFOQueueUrl:
    Description: SQS.FIFO.QueueUrl
    Value: !Ref microservicesDrawQueueFIFO
  TopicARN:
    Description: SNS.TopicARN
    Value: !Ref microservicesDrawTopic
  CognitoIdentityPoolId:
    Description: Cognito.IdentityPoolId
    Value: !Ref CIPMessageDraw

  AWSAccessKey:
    Value: !Ref AWSAccessKey
  AWSSecretAccessKey:
    Value: !GetAtt AWSAccessKey.SecretAccessKey

  AccountID:
    Value: !Ref AWS::AccountId

  Region:
    Value: !Ref AWS::Region
