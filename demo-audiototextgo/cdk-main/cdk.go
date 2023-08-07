package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsiam"
	"github.com/aws/aws-cdk-go/awscdk/v2/awslambda"
	"github.com/aws/aws-cdk-go/awscdk/v2/awslambdaeventsources"
	"github.com/aws/aws-cdk-go/awscdk/v2/awss3"
	"github.com/aws/aws-cdk-go/awscdklambdagoalpha/v2"

	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

const functionDir = "../cdk-support"

type LambdaTranscribeAudioToTextGolangStackProps struct {
	awscdk.StackProps
}

func demotranscribeaudiototextgo(scope constructs.Construct, id string, props *LambdaTranscribeAudioToTextGolangStackProps) awscdk.Stack {
	var sprops awscdk.StackProps
	if props != nil {
		sprops = props.StackProps
	}
	stack := awscdk.NewStack(scope, &id, &sprops)

	sourceBucket := awss3.NewBucket(stack, jsii.String("source-bucket"), &awss3.BucketProps{
		BlockPublicAccess: awss3.BlockPublicAccess_BLOCK_ALL(),
		RemovalPolicy:     awscdk.RemovalPolicy_DESTROY,
		AutoDeleteObjects: jsii.Bool(true),
		//BucketName:        jsii.String("demo-source"),
	})

	outputBucket := awss3.NewBucket(stack, jsii.String("destination-bucket"), &awss3.BucketProps{
		BlockPublicAccess: awss3.BlockPublicAccess_BLOCK_ALL(),
		RemovalPolicy:     awscdk.RemovalPolicy_DESTROY,
		AutoDeleteObjects: jsii.Bool(true),
		//BucketName:        jsii.String("demo-destination"),
	})

	function := awscdklambdagoalpha.NewGoFunction(stack, jsii.String("function"),
		&awscdklambdagoalpha.GoFunctionProps{
			Runtime:     awslambda.Runtime_GO_1_X(),
			Environment: &map[string]*string{"OUTPUT_BUCKET_NAME": outputBucket.BucketName()},
			Entry:       jsii.String(functionDir),
		})

	//the roles that are granted are more than what's required. homework for reader to make this fine-grained

	sourceBucket.GrantRead(function, "*")
	outputBucket.GrantReadWrite(function, "*")
	function.Role().AddManagedPolicy(awsiam.ManagedPolicy_FromAwsManagedPolicyName(jsii.String("AmazonTranscribeFullAccess")))

	function.AddEventSource(awslambdaeventsources.NewS3EventSource(sourceBucket, &awslambdaeventsources.S3EventSourceProps{
		Events: &[]awss3.EventType{awss3.EventType_OBJECT_CREATED},
	}))

	awscdk.NewCfnOutput(stack, jsii.String("demo-source"),
		&awscdk.CfnOutputProps{
			ExportName: jsii.String("demo-source"),
			Value:      sourceBucket.BucketName()})

	awscdk.NewCfnOutput(stack, jsii.String("demo-destination"),
		&awscdk.CfnOutputProps{
			ExportName: jsii.String("demo-destination"),
			Value:      outputBucket.BucketName()})

	return stack
}

func main() {
	app := awscdk.NewApp(nil)

	demotranscribeaudiototextgo(app, "demo-audiototextgo", &LambdaTranscribeAudioToTextGolangStackProps{
		awscdk.StackProps{
			Env: env(),
		},
	})

	app.Synth(nil)
}

func env() *awscdk.Environment {
	return nil
}
