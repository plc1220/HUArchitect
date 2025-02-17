# ALIBABACLOUD
from diagrams.alibabacloud.analytics import AnalyticDb, ClickHouse, DataLakeAnalytics,
    ElaticMapReduce, OpenSearch
from diagrams.alibabacloud.application import ApiGateway, BeeBot, BlockchainAsAService,
    CloudCallCenter, CodePipeline, DirectMail, LogService, MNS, MessageNotificationService,
    NodeJsPerformancePlatform, OpenSearch, PTS, PerformanceTestingService, RdCloud, SCA, SLS,
    SmartConversationAnalysis, Yida
from diagrams.alibabacloud.communication import DirectMail, MobilePush
from diagrams.alibabacloud.compute import AutoScaling, BatchCompute, ContainerRegistry,
    ContainerService, ECI, ECS, EHPC, ESS, ElasticComputeService, ElasticContainerInstance,
    ElasticHighPerformanceComputing, ElasticSearch, FC, FunctionCompute, OOS,
    OperationOrchestrationService, ROS, ResourceOrchestrationService, SAE, SAS, SLB,
    ServerLoadBalancer, ServerlessAppEngine, SimpleApplicationServer, WAS, WebAppService
from diagrams.alibabacloud.database import ApsaradbCassandra, ApsaradbHbase, ApsaradbMemcache,
    ApsaradbMongodb, ApsaradbOceanbase, ApsaradbPolardb, ApsaradbPostgresql, ApsaradbPpas,
    ApsaradbRedis, ApsaradbSqlserver, DBS, DMS, DRDS, DTS, DataManagementService,
    DataTransmissionService, DatabaseBackupService, DisributeRelationalDatabaseService, GDS,
    GraphDatabaseService, HybriddbForMysql, RDS, RelationalDatabaseService
from diagrams.alibabacloud.iot import IotInternetDeviceId, IotLinkWan, IotMobileConnectionPackage,
    IotPlatform
from diagrams.alibabacloud.network import CEN, Cdn, CloudEnterpriseNetwork, EIP, ElasticIpAddress,
    ExpressConnect, NatGateway, SLB, ServerLoadBalancer, SmartAccessGateway, VPC,
    VirtualPrivateCloud, VpnGateway
from diagrams.alibabacloud.security import ABS, AS, AntiBotService, AntiDdosBasic, AntiDdosPro,
    AntifraudService, BastionHost, CFW, CM, CloudFirewall, CloudSecurityScanner, ContentModeration,
    CrowdsourcedSecurityTesting, DES, DataEncryptionService, DbAudit, GameShield, IdVerification,
    ManagedSecurityService, SecurityCenter, ServerGuard, SslCertificates, WAF,
    WebApplicationFirewall
from diagrams.alibabacloud.storage import CloudStorageGateway, FileStorageHdfs, FileStorageNas, HBR,
    HDFS, HDR, HybridBackupRecovery, HybridCloudDisasterRecovery, Imm, NAS, OSS, OTS,
    ObjectStorageService, ObjectTableStore
from diagrams.alibabacloud.web import Dns, Domain

# AWS
from diagrams.aws.analytics import AmazonOpensearchService, Analytics, Athena, Cloudsearch,
    CloudsearchSearchDocuments, DataLakeResource, DataPipeline, EMR, EMRCluster, EMREngine,
    EMREngineMaprM3, EMREngineMaprM5, EMREngineMaprM7, EMRHdfsCluster, ES, ElasticsearchService,
    Glue, GlueCrawlers, GlueDataCatalog, Kinesis, KinesisDataAnalytics, KinesisDataFirehose,
    KinesisDataStreams, KinesisVideoStreams, LakeFormation, ManagedStreamingForKafka, Quicksight,
    Redshift, RedshiftDenseComputeNode, RedshiftDenseStorageNode
from diagrams.aws.ar import ArVr, Sumerian
from diagrams.aws.blockchain import Blockchain, BlockchainResource, ManagedBlockchain, QLDB,
    QuantumLedgerDatabaseQldb
from diagrams.aws.business import A4B, AlexaForBusiness, BusinessApplications, Chime, Workmail
from diagrams.aws.compute import AMI, AppRunner, ApplicationAutoScaling, AutoScaling, Batch,
    Compute, ComputeOptimizer, EB, EC2, EC2Ami, EC2AutoScaling, EC2ContainerRegistry,
    EC2ContainerRegistryImage, EC2ContainerRegistryRegistry, EC2ElasticIpAddress, EC2ImageBuilder,
    EC2Instance, EC2Instances, EC2Rescue, EC2SpotInstance, ECR, ECS, EKS, ElasticBeanstalk,
    ElasticBeanstalkApplication, ElasticBeanstalkDeployment, ElasticContainerService,
    ElasticContainerServiceContainer, ElasticContainerServiceService, ElasticKubernetesService,
    Fargate, Lambda, LambdaFunction, Lightsail, LocalZones, Outposts, SAR,
    ServerlessApplicationRepository, ThinkboxDeadline, ThinkboxDraft, ThinkboxFrost,
    ThinkboxKrakatoa, ThinkboxSequoia, ThinkboxStoke, ThinkboxXmesh, VmwareCloudOnAWS, Wavelength
from diagrams.aws.cost import Budgets, CostAndUsageReport, CostExplorer, CostManagement,
    ReservedInstanceReporting, SavingsPlans
from diagrams.aws.database import Aurora, AuroraInstance, DAX, DB, DDB, DMS, Database,
    DatabaseMigrationService, DatabaseMigrationServiceDatabaseMigrationWorkflow, DocumentDB,
    DocumentdbMongodbCompatibility, Dynamodb, DynamodbAttribute, DynamodbAttributes, DynamodbDax,
    DynamodbGSI, DynamodbGlobalSecondaryIndex, DynamodbItem, DynamodbItems, DynamodbTable,
    ElastiCache, Elasticache, ElasticacheCacheNode, ElasticacheForMemcached, ElasticacheForRedis,
    KeyspacesManagedApacheCassandraService, Neptune, QLDB, QuantumLedgerDatabaseQldb, RDS,
    RDSInstance, RDSMariadbInstance, RDSMysqlInstance, RDSOnVmware, RDSOracleInstance,
    RDSPostgresqlInstance, RDSSqlServerInstance, Redshift, RedshiftDenseComputeNode,
    RedshiftDenseStorageNode, Timestream
from diagrams.aws.devtools import CLI, Cloud9, Cloud9Resource, CloudDevelopmentKit, Codeartifact,
    Codebuild, Codecommit, Codedeploy, Codepipeline, Codestar, CommandLineInterface, DevTools,
    DeveloperTools, ToolsAndSdks, XRay
from diagrams.aws.enablement import CustomerEnablement, Iq, ManagedServices, ProfessionalServices,
    Support
from diagrams.aws.enduser import Appstream20, DesktopAndAppStreaming, Workdocs, Worklink, Workspaces
from diagrams.aws.engagement import Connect, CustomerEngagement, Pinpoint, SES,
    SimpleEmailServiceSes, SimpleEmailServiceSesEmail
from diagrams.aws.game import GameTech, Gamelift
from diagrams.aws.general import Client, Disk, Forums, General, GenericDatabase, GenericFirewall,
    GenericOfficeBuilding, GenericSDK, GenericSamlToken, InternetAlt1, InternetAlt2,
    InternetGateway, Marketplace, MobileClient, Multimedia, OfficeBuilding, SDK, SamlToken,
    SslPadlock, TapeStorage, Toolkit, TraditionalServer, User, Users
from diagrams.aws.integration import ApplicationIntegration, Appsync, ConsoleMobileApplication,
    EventResource, Eventbridge, EventbridgeCustomEventBusResource,
    EventbridgeDefaultEventBusResource, EventbridgeSaasPartnerEventBusResource, ExpressWorkflows,
    MQ, SF, SNS, SQS, SimpleNotificationServiceSns, SimpleNotificationServiceSnsEmailNotification,
    SimpleNotificationServiceSnsHttpNotification, SimpleNotificationServiceSnsTopic,
    SimpleQueueServiceSqs, SimpleQueueServiceSqsMessage, SimpleQueueServiceSqsQueue, StepFunctions
from diagrams.aws.iot import FreeRTOS, Freertos, InternetOfThings, Iot1Click, IotAction,
    IotActuator, IotAlexaEcho, IotAlexaEnabledDevice, IotAlexaSkill, IotAlexaVoiceService,
    IotAnalytics, IotAnalyticsChannel, IotAnalyticsDataSet, IotAnalyticsDataStore,
    IotAnalyticsNotebook, IotAnalyticsPipeline, IotBank, IotBicycle, IotBoard, IotButton, IotCamera,
    IotCar, IotCart, IotCertificate, IotCoffeePot, IotCore, IotDesiredState, IotDeviceDefender,
    IotDeviceGateway, IotDeviceManagement, IotDoorLock, IotEvents, IotFactory, IotFireTv,
    IotFireTvStick, IotGeneric, IotGreengrass, IotGreengrassConnector, IotHardwareBoard, IotHouse,
    IotHttp, IotHttp2, IotJobs, IotLambda, IotLightbulb, IotMedicalEmergency, IotMqtt,
    IotOverTheAirUpdate, IotPolicy, IotPolicyEmergency, IotReportedState, IotRule, IotSensor,
    IotServo, IotShadow, IotSimulator, IotSitewise, IotThermostat, IotThingsGraph, IotTopic,
    IotTravel, IotUtility, IotWindfarm
from diagrams.aws.management import AmazonDevopsGuru, AmazonManagedGrafana, AmazonManagedPrometheus,
    AmazonManagedWorkflowsApacheAirflow, AutoScaling, Chatbot, Cloudformation,
    CloudformationChangeSet, CloudformationStack, CloudformationTemplate, Cloudtrail, Cloudwatch,
    CloudwatchAlarm, CloudwatchEventEventBased, CloudwatchEventTimeBased, CloudwatchRule, Codeguru,
    CommandLineInterface, Config, ControlTower, LicenseManager, ManagedServices,
    ManagementAndGovernance, ManagementConsole, Opsworks, OpsworksApps, OpsworksDeployments,
    OpsworksInstances, OpsworksLayers, OpsworksMonitoring, OpsworksPermissions, OpsworksResources,
    OpsworksStack, Organizations, OrganizationsAccount, OrganizationsOrganizationalUnit,
    ParameterStore, PersonalHealthDashboard, Proton, SSM, ServiceCatalog, SystemsManager,
    SystemsManagerAppConfig, SystemsManagerAutomation, SystemsManagerDocuments,
    SystemsManagerInventory, SystemsManagerMaintenanceWindows, SystemsManagerOpscenter,
    SystemsManagerParameterStore, SystemsManagerPatchManager, SystemsManagerRunCommand,
    SystemsManagerStateManager, TrustedAdvisor, TrustedAdvisorChecklist,
    TrustedAdvisorChecklistCost, TrustedAdvisorChecklistFaultTolerant,
    TrustedAdvisorChecklistPerformance, TrustedAdvisorChecklistSecurity, WellArchitectedTool
from diagrams.aws.media import ElasticTranscoder, ElementalConductor, ElementalDelta, ElementalLive,
    ElementalMediaconnect, ElementalMediaconvert, ElementalMedialive, ElementalMediapackage,
    ElementalMediastore, ElementalMediatailor, ElementalServer, KinesisVideoStreams, MediaServices
from diagrams.aws.migration import ADS, ApplicationDiscoveryService, CEM, CloudendureMigration, DMS,
    DatabaseMigrationService, Datasync, DatasyncAgent, MAT, MigrationAndTransfer, MigrationHub, SMS,
    ServerMigrationService, Snowball, SnowballEdge, Snowmobile, TransferForSftp
from diagrams.aws.ml import ApacheMxnetOnAWS, AugmentedAi, Comprehend, DLC, DeepLearningAmis,
    DeepLearningContainers, Deepcomposer, Deeplens, Deepracer, ElasticInference, Forecast,
    FraudDetector, Kendra, Lex, MachineLearning, Personalize, Polly, Rekognition, RekognitionImage,
    RekognitionVideo, Sagemaker, SagemakerGroundTruth, SagemakerModel, SagemakerNotebook,
    SagemakerTrainingJob, TensorflowOnAWS, Textract, Transcribe, Translate
from diagrams.aws.mobile import APIGateway, APIGatewayEndpoint, Amplify, Appsync, DeviceFarm,
    Mobile, Pinpoint
from diagrams.aws.network import ALB, APIGateway, APIGatewayEndpoint, AppMesh, CF, CLB, ClientVpn,
    CloudFront, CloudFrontDownloadDistribution, CloudFrontEdgeLocation,
    CloudFrontStreamingDistribution, CloudMap, DirectConnect, ELB, ElasticLoadBalancing,
    ElbApplicationLoadBalancer, ElbClassicLoadBalancer, ElbNetworkLoadBalancer, Endpoint, GAX,
    GlobalAccelerator, InternetGateway, NATGateway, NLB, Nacl, NetworkFirewall,
    NetworkingAndContentDelivery, PrivateSubnet, Privatelink, PublicSubnet, Route53,
    Route53HostedZone, RouteTable, SiteToSiteVpn, TransitGateway, VPC, VPCCustomerGateway,
    VPCElasticNetworkAdapter, VPCElasticNetworkInterface, VPCFlowLogs, VPCPeering, VPCRouter,
    VPCTrafficMirroring, VpnConnection, VpnGateway
from diagrams.aws.quantum import Braket, QuantumTechnologies
from diagrams.aws.robotics import Robomaker, RobomakerCloudExtensionRos,
    RobomakerDevelopmentEnvironment, RobomakerFleetManagement, RobomakerSimulator, Robotics
from diagrams.aws.satellite import GroundStation, Satellite
from diagrams.aws.security import ACM, AdConnector, Artifact, CertificateAuthority,
    CertificateManager, CloudDirectory, CloudHSM, Cloudhsm, Cognito, DS, Detective,
    DirectoryService, FMS, FirewallManager, Guardduty, IAM, IAMAWSSts, IAMAccessAnalyzer,
    IAMPermissions, IAMRole, IdentityAndAccessManagementIam, IdentityAndAccessManagementIamAWSSts,
    IdentityAndAccessManagementIamAWSStsAlternate, IdentityAndAccessManagementIamAccessAnalyzer,
    IdentityAndAccessManagementIamAddOn, IdentityAndAccessManagementIamDataEncryptionKey,
    IdentityAndAccessManagementIamEncryptedData,
    IdentityAndAccessManagementIamLongTermSecurityCredential,
    IdentityAndAccessManagementIamMfaToken, IdentityAndAccessManagementIamPermissions,
    IdentityAndAccessManagementIamRole, IdentityAndAccessManagementIamTemporarySecurityCredential,
    Inspector, InspectorAgent, KMS, KeyManagementService, Macie, ManagedMicrosoftAd, RAM,
    ResourceAccessManager, SecretsManager, SecurityHub, SecurityHubFinding,
    SecurityIdentityAndCompliance, Shield, ShieldAdvanced, SimpleAd, SingleSignOn, WAF,
    WAFFilteringRule
from diagrams.aws.storage import Backup, CDR, CloudendureDisasterRecovery, EBS, EFS,
    EFSInfrequentaccessPrimaryBg, EFSStandardPrimaryBg, ElasticBlockStoreEBS,
    ElasticBlockStoreEBSSnapshot, ElasticBlockStoreEBSVolume, ElasticFileSystemEFS,
    ElasticFileSystemEFSFileSystem, FSx, Fsx, FsxForLustre, FsxForWindowsFileServer,
    MultipleVolumesResource, S3, S3Glacier, S3GlacierArchive, S3GlacierVault,
    SimpleStorageServiceS3, SimpleStorageServiceS3Bucket, SimpleStorageServiceS3BucketWithObjects,
    SimpleStorageServiceS3Object, SnowFamilySnowballImportExport, Snowball, SnowballEdge,
    Snowmobile, Storage, StorageGateway, StorageGatewayCachedVolume, StorageGatewayNonCachedVolume,
    StorageGatewayVirtualTapeLibrary

# AZURE
from diagrams.azure.analytics import AnalysisServices, DataExplorerClusters, DataFactories,
    DataLakeAnalytics, DataLakeStoreGen1, Databricks, EventHubClusters, EventHubs,
    Hdinsightclusters, LogAnalyticsWorkspaces, StreamAnalyticsJobs, SynapseAnalytics
from diagrams.azure.compute import ACR, AKS, AppServices, AutomanagedVM, AvailabilitySets,
    BatchAccounts, CitrixVirtualDesktopsEssentials, CloudServices, CloudServicesClassic,
    CloudsimpleVirtualMachines, ContainerApps, ContainerInstances, ContainerRegistries,
    DiskEncryptionSets, DiskSnapshots, Disks, FunctionApps, ImageDefinitions, ImageVersions,
    KubernetesServices, MeshApplications, OsImages, SAPHANAOnAzure, ServiceFabricClusters,
    SharedImageGalleries, SpringCloud, VM, VMClassic, VMImages, VMLinux, VMSS, VMScaleSet,
    VMWindows, Workspaces
from diagrams.azure.database import BlobStorage, CacheForRedis, CosmosDb, DataExplorerClusters,
    DataFactory, DataLake, DatabaseForMariadbServers, DatabaseForMysqlServers,
    DatabaseForPostgresqlServers, ElasticDatabasePools, ElasticJobAgents, InstancePools,
    ManagedDatabases, SQL, SQLDatabases, SQLDatawarehouse, SQLManagedInstances,
    SQLServerStretchDatabases, SQLServers, SQLVM, SsisLiftAndShiftIr, SynapseAnalytics,
    VirtualClusters, VirtualDatacenter
from diagrams.azure.devops import ApplicationInsights, Artifacts, Boards, Devops, DevtestLabs,
    LabServices, Pipelines, Repos, TestPlans
from diagrams.azure.general import Allresources, Azurehome, Developertools, Helpsupport,
    Information, Managementgroups, Marketplace, Quickstartcenter, Recent, Reservations, Resource,
    Resourcegroups, Servicehealth, Shareddashboard, Subscriptions, Support, Supportrequests, Tag,
    Tags, Templates, Twousericon, Userhealthicon, Usericon, Userprivacy, Userresource, Whatsnew
from diagrams.azure.identity import ADB2C, ADDomainServices, ADIdentityProtection,
    ADPrivilegedIdentityManagement, AccessReview, ActiveDirectory, ActiveDirectoryConnectHealth,
    AppRegistrations, ConditionalAccess, EnterpriseApplications, Groups, IdentityGovernance,
    InformationProtection, ManagedIdentities, Users
from diagrams.azure.integration import APIForFhir, APIManagement, AppConfiguration, DataCatalog,
    EventGridDomains, EventGridSubscriptions, EventGridTopics, IntegrationAccounts,
    IntegrationServiceEnvironments, LogicApps, LogicAppsCustomConnector, PartnerTopic,
    SendgridAccounts, ServiceBus, ServiceBusRelays, ServiceCatalogManagedApplicationDefinitions,
    SoftwareAsAService, StorsimpleDeviceManagers, SystemTopic
from diagrams.azure.iot import DeviceProvisioningServices, DigitalTwins, IotCentralApplications,
    IotHub, IotHubSecurity, Maps, Sphere, TimeSeriesInsightsEnvironments,
    TimeSeriesInsightsEventsSources, Windows10IotCoreServices
from diagrams.azure.migration import DataBox, DataBoxEdge, DatabaseMigrationServices,
    MigrationProjects, RecoveryServicesVaults
from diagrams.azure.ml import BatchAI, BotServices, CognitiveServices, GenomicsAccounts,
    MachineLearningServiceWorkspaces, MachineLearningStudioWebServicePlans,
    MachineLearningStudioWebServices, MachineLearningStudioWorkspaces
from diagrams.azure.mobile import AppServiceMobile, MobileEngagement, NotificationHubs
from diagrams.azure.monitor import ChangeAnalysis, Logs, Metrics, Monitor
from diagrams.azure.network import ApplicationGateway, ApplicationSecurityGroups, CDNProfiles,
    Connections, DDOSProtectionPlans, DNSPrivateZones, DNSZones, ExpressrouteCircuits, Firewall,
    FrontDoors, LoadBalancers, LocalNetworkGateways, NetworkInterfaces,
    NetworkSecurityGroupsClassic, NetworkWatcher, OnPremisesDataGateways, PrivateEndpoint,
    PublicIpAddresses, ReservedIpAddressesClassic, RouteFilters, RouteTables,
    ServiceEndpointPolicies, Subnets, TrafficManagerProfiles, VirtualNetworkClassic,
    VirtualNetworkGateways, VirtualNetworks, VirtualWans
from diagrams.azure.security import ApplicationSecurityGroups, ConditionalAccess, Defender,
    ExtendedSecurityUpdates, KeyVaults, SecurityCenter, Sentinel
from diagrams.azure.storage import ArchiveStorage, Azurefxtedgefiler, BlobStorage, DataBox,
    DataBoxEdgeDataBoxGateway, DataLakeStorage, GeneralStorage, NetappFiles, QueuesStorage,
    StorageAccounts, StorageAccountsClassic, StorageExplorer, StorageSyncServices,
    StorsimpleDataManagers, StorsimpleDeviceManagers, TableStorage
from diagrams.azure.web import APIConnections, AppServiceCertificates, AppServiceDomains,
    AppServiceEnvironments, AppServicePlans, AppServices, MediaServices, NotificationHubNamespaces,
    Search, Signalr

# BASE

# C4

# CUSTOM

# DIGITALOCEAN
from diagrams.digitalocean.compute import Containers, Docker, Droplet, DropletConnect,
    DropletSnapshot, K8SCluster, K8SNode, K8SNodePool
from diagrams.digitalocean.database import DbaasPrimary, DbaasPrimaryStandbyMore, DbaasReadOnly,
    DbaasStandby
from diagrams.digitalocean.network import Certificate, Domain, DomainRegistration, Firewall,
    FloatingIp, InternetGateway, LoadBalancer, ManagedVpn, Vpc
from diagrams.digitalocean.storage import Folder, Space, Volume, VolumeSnapshot

# ELASTIC
from diagrams.elastic.agent import Agent, Endpoint, Fleet, Integrations
from diagrams.elastic.beats import APM, Auditbeat, Filebeat, Functionbeat, Heartbeat, Metricbeat,
    Packetbeat, Winlogbeat
from diagrams.elastic.elasticsearch import Alerting, Beats, ElasticSearch, Elasticsearch, Kibana,
    LogStash, Logstash, LogstashPipeline, ML, MachineLearning, MapServices, Maps, Monitoring, SQL,
    SearchableSnapshots, SecuritySettings, Stack
from diagrams.elastic.enterprisesearch import AppSearch, Crawler, EnterpriseSearch, SiteSearch,
    WorkplaceSearch
from diagrams.elastic.observability import APM, Logs, Metrics, Observability, Uptime
from diagrams.elastic.orchestration import ECE, ECK
from diagrams.elastic.saas import Cloud, Elastic
from diagrams.elastic.security import Endpoint, SIEM, Security, Xdr

# FIREBASE
from diagrams.firebase.base import Firebase
from diagrams.firebase.develop import Authentication, Firestore, Functions, Hosting, MLKit,
    RealtimeDatabase, Storage
from diagrams.firebase.extentions import Extensions
from diagrams.firebase.grow import ABTesting, AppIndexing, DynamicLinks, FCM, InAppMessaging,
    Invites, Messaging, Predictions, RemoteConfig
from diagrams.firebase.quality import AppDistribution, CrashReporting, Crashlytics,
    PerformanceMonitoring, TestLab

# GCP
from diagrams.gcp.analytics import BigQuery, Bigquery, Composer, DataCatalog, DataFusion, Dataflow,
    Datalab, Dataprep, Dataproc, Genomics, PubSub, Pubsub
from diagrams.gcp.api import APIGateway, Apigee, Endpoints
from diagrams.gcp.compute import AppEngine, ComputeEngine, ContainerOptimizedOS, Functions, GAE,
    GCE, GCF, GKE, GKEOnPrem, GPU, KubernetesEngine, Run
from diagrams.gcp.database import BigTable, Bigtable, Datastore, Firestore, Memorystore, SQL,
    Spanner
from diagrams.gcp.devtools import Build, Code, CodeForIntellij, ContainerRegistry, GCR,
    GradleAppEnginePlugin, IdePlugins, MavenAppEnginePlugin, SDK, Scheduler, SourceRepositories,
    Tasks, TestLab, ToolsForEclipse, ToolsForPowershell, ToolsForVisualStudio
from diagrams.gcp.iot import IotCore
from diagrams.gcp.migration import TransferAppliance
from diagrams.gcp.ml import AIHub, AIPlatform, AIPlatformDataLabelingService, AdvancedSolutionsLab,
    AutoML, Automl, AutomlNaturalLanguage, AutomlTables, AutomlTranslation, AutomlVideoIntelligence,
    AutomlVision, DialogFlowEnterpriseEdition, InferenceAPI, JobsAPI, NLAPI, NaturalLanguageAPI,
    RecommendationsAI, STT, SpeechToText, TPU, TTS, TextToSpeech, TranslationAPI,
    VideoIntelligenceAPI, VisionAPI
from diagrams.gcp.network import Armor, CDN, DNS, DedicatedInterconnect, ExternalIpAddresses,
    FirewallRules, LoadBalancing, NAT, Network, PartnerInterconnect, PremiumNetworkTier, Router,
    Routes, StandardNetworkTier, TrafficDirector, VPC, VPN, VirtualPrivateCloud
from diagrams.gcp.operations import Logging, Monitoring
from diagrams.gcp.security import IAP, Iam, KMS, KeyManagementService, ResourceManager, SCC,
    SecurityCommandCenter, SecurityScanner
from diagrams.gcp.storage import Filestore, GCS, PersistentDisk, Storage

# GENERIC
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.device import Mobile, Tablet
from diagrams.generic.network import Firewall, Router, Subnet, Switch, VPN
from diagrams.generic.os import Android, Centos, Debian, IOS, LinuxGeneral, Raspbian, RedHat, Suse,
    Ubuntu, Windows
from diagrams.generic.place import Datacenter
from diagrams.generic.storage import Storage
from diagrams.generic.virtualization import Qemu, Virtualbox, Vmware, XEN

# IBM
from diagrams.ibm.analytics import Analytics, DataIntegration, DataRepositories, DeviceAnalytics,
    StreamingComputing
from diagrams.ibm.applications import ActionableInsight, Annotate, ApiDeveloperPortal,
    ApiPolyglotRuntimes, AppServer, ApplicationLogic, EnterpriseApplications, Index, IotApplication,
    Microservice, MobileApp, Ontology, OpenSourceTools, RuntimeServices, SaasApplications,
    ServiceBroker, SpeechToText, VisualRecognition, Visualization
from diagrams.ibm.blockchain import Blockchain, BlockchainDeveloper, CertificateAuthority,
    ClientApplication, Communication, Consensus, Event, EventListener, ExistingEnterpriseSystems,
    HyperledgerFabric, KeyManagement, Ledger, Membership, MembershipServicesProviderApi, MessageBus,
    Node, Services, SmartContract, TransactionManager, Wallet
from diagrams.ibm.compute import BareMetalServer, ImageService, Instance, Key, PowerInstance
from diagrams.ibm.data import Caches, Cloud, ConversationTrainedDeployed, DataServices, DataSources,
    DeviceIdentityService, DeviceRegistry, EnterpriseData, EnterpriseUserDirectory, FileRepository,
    GroundTruth, Model, TmsDataInterface
from diagrams.ibm.devops import ArtifactManagement, BuildTest, CodeEditor, CollaborativeDevelopment,
    ConfigurationManagement, ContinuousDeploy, ContinuousTesting, Devops, Provision,
    ReleaseManagement
from diagrams.ibm.general import CloudMessaging, CloudServices, Cloudant, CognitiveServices,
    DataSecurity, Enterprise, GovernanceRiskCompliance, IBMContainers, IBMPublicCloud,
    IdentityAccessManagement, IdentityProvider, InfrastructureSecurity, Internet, IotCloud,
    MicroservicesApplication, MicroservicesMesh, Monitoring, MonitoringLogging, ObjectStorage,
    OfflineCapabilities, Openwhisk, PeerCloud, RetrieveRank, Scalable,
    ServiceDiscoveryConfiguration, TextToSpeech, TransformationConnectivity
from diagrams.ibm.infrastructure import Channels, CloudMessaging, Dashboard, Diagnostics,
    EdgeServices, EnterpriseMessaging, EventFeed, InfrastructureServices, InterserviceCommunication,
    LoadBalancingRouting, MicroservicesMesh, MobileBackend, MobileProviderNetwork, Monitoring,
    MonitoringLogging, PeerServices, ServiceDiscoveryConfiguration, TransformationConnectivity
from diagrams.ibm.management import AlertNotification, ApiManagement, CloudManagement,
    ClusterManagement, ContentManagement, DataServices, DeviceManagement, InformationGovernance,
    ItServiceManagement, Management, MonitoringMetrics, ProcessManagement,
    ProviderCloudPortalService, PushNotifications, ServiceManagementTools
from diagrams.ibm.network import Bridge, DirectLink, Enterprise, Firewall, FloatingIp, Gateway,
    InternetServices, LoadBalancer, LoadBalancerListener, LoadBalancerPool, LoadBalancingRouting,
    PublicGateway, Region, Router, Rules, Subnet, TransitGateway, Vpc, VpnConnection, VpnGateway,
    VpnPolicy
from diagrams.ibm.security import ApiSecurity, BlockchainSecurityService, DataSecurity, Firewall,
    Gateway, GovernanceRiskCompliance, IdentityAccessManagement, IdentityProvider,
    InfrastructureSecurity, PhysicalSecurity, SecurityMonitoringIntelligence, SecurityServices,
    TrustendComputing, Vpn
from diagrams.ibm.social import Communities, FileSync, LiveCollaboration, Messaging, Networking
from diagrams.ibm.storage import BlockStorage, ObjectStorage
from diagrams.ibm.user import Browser, Device, IntegratedDigitalExperiences, PhysicalEntity, Sensor,
    User

# K8S
from diagrams.k8s.chaos import ChaosMesh, LitmusChaos
from diagrams.k8s.clusterconfig import HPA, HorizontalPodAutoscaler, LimitRange, Limits, Quota
from diagrams.k8s.compute import Cronjob, DS, DaemonSet, Deploy, Deployment, Job, Pod, RS,
    ReplicaSet, STS, StatefulSet
from diagrams.k8s.controlplane import API, APIServer, CCM, CM, ControllerManager, KProxy, KubeProxy,
    Kubelet, Sched, Scheduler
from diagrams.k8s.ecosystem import ExternalDns, Helm, Krew, Kustomize
from diagrams.k8s.group import NS, Namespace
from diagrams.k8s.infra import ETCD, Master, Node
from diagrams.k8s.network import Endpoint, Ep, Ing, Ingress, Netpol, NetworkPolicy, SVC, Service
from diagrams.k8s.others import CRD, PSP
from diagrams.k8s.podconfig import CM, ConfigMap, Secret
from diagrams.k8s.rbac import CRB, CRole, ClusterRole, ClusterRoleBinding, Group, RB, Role,
    RoleBinding, SA, ServiceAccount, User
from diagrams.k8s.storage import PV, PVC, PersistentVolume, PersistentVolumeClaim, SC, StorageClass,
    Vol, Volume

# OCI
from diagrams.oci.compute import Autoscale, AutoscaleWhite, BM, BMWhite, BareMetal, BareMetalWhite,
    Container, ContainerEngine, ContainerEngineWhite, ContainerWhite, Functions, FunctionsWhite,
    InstancePools, InstancePoolsWhite, OCIR, OCIRWhite, OCIRegistry, OCIRegistryWhite, OKE,
    OKEWhite, VM, VMWhite, VirtualMachine, VirtualMachineWhite
from diagrams.oci.connectivity import Backbone, BackboneWhite, CDN, CDNWhite, CustomerDatacenter,
    CustomerDatacntrWhite, CustomerPremises, CustomerPremisesWhite, DNS, DNSWhite,
    DisconnectedRegions, DisconnectedRegionsWhite, FastConnect, FastConnectWhite, NATGateway,
    NATGatewayWhite, VPN, VPNWhite
from diagrams.oci.database import ADB, ADBWhite, Autonomous, AutonomousWhite, BigdataService,
    BigdataServiceWhite, DBService, DBServiceWhite, DMS, DMSWhite, DatabaseService,
    DatabaseServiceWhite, DataflowApache, DataflowApacheWhite, Dcat, DcatWhite, Dis, DisWhite,
    Science, ScienceWhite, Stream, StreamWhite
from diagrams.oci.devops import APIGateway, APIGatewayWhite, APIService, APIServiceWhite,
    ResourceMgmt, ResourceMgmtWhite
from diagrams.oci.governance import Audit, AuditWhite, Compartments, CompartmentsWhite, Groups,
    GroupsWhite, Logging, LoggingWhite, OCID, OCIDWhite, Policies, PoliciesWhite, Tagging,
    TaggingWhite
from diagrams.oci.monitoring import Alarm, AlarmWhite, Email, EmailWhite, Events, EventsWhite,
    HealthCheck, HealthCheckWhite, Notifications, NotificationsWhite, Queue, QueueWhite, Search,
    SearchWhite, Telemetry, TelemetryWhite, Workflow, WorkflowWhite
from diagrams.oci.network import Drg, DrgWhite, Firewall, FirewallWhite, InternetGateway,
    InternetGatewayWhite, LoadBalancer, LoadBalancerWhite, RouteTable, RouteTableWhite,
    SecurityLists, SecurityListsWhite, ServiceGateway, ServiceGatewayWhite, Vcn, VcnWhite
from diagrams.oci.security import CloudGuard, CloudGuardWhite, DDOS, DDOSWhite, Encryption,
    EncryptionWhite, IDAccess, IDAccessWhite, KeyManagement, KeyManagementWhite, MaxSecurityZone,
    MaxSecurityZoneWhite, Vault, VaultWhite, WAF, WAFWhite
from diagrams.oci.storage import BackupRestore, BackupRestoreWhite, BlockStorage, BlockStorageClone,
    BlockStorageCloneWhite, BlockStorageWhite, Buckets, BucketsWhite, DataTransfer,
    DataTransferWhite, ElasticPerformance, ElasticPerformanceWhite, FileStorage, FileStorageWhite,
    ObjectStorage, ObjectStorageWhite, StorageGateway, StorageGatewayWhite

# ONPREM
from diagrams.onprem.aggregator import Fluentd, Vector
from diagrams.onprem.analytics import Beam, Databricks, Dbt, Dremio, Flink, Hadoop, Hive, Metabase,
    Norikra, PowerBI, Powerbi, Presto, Singer, Spark, Storm, Superset, Tableau, Trino
from diagrams.onprem.auth import Boundary, BuzzfeedSso, Oauth2Proxy
from diagrams.onprem.cd import Spinnaker, Tekton, TektonCli
from diagrams.onprem.certificates import CertManager, LetsEncrypt
from diagrams.onprem.ci import CircleCI, Circleci, ConcourseCI, Concourseci, DroneCI, Droneci,
    GithubActions, GitlabCI, Gitlabci, Jenkins, TC, Teamcity, TravisCI, Travisci, ZuulCI, Zuulci
from diagrams.onprem.client import Client, User, Users
from diagrams.onprem.compute import Nomad, Server
from diagrams.onprem.container import Containerd, Crio, Docker, Firecracker, Gvisor, K3S, LXC, Lxc,
    RKT, Rkt
from diagrams.onprem.database import Cassandra, ClickHouse, Clickhouse, CockroachDB, Cockroachdb,
    CouchDB, Couchbase, Couchdb, Dgraph, Druid, HBase, Hbase, InfluxDB, Influxdb, JanusGraph,
    Janusgraph, MSSQL, MariaDB, Mariadb, MongoDB, Mongodb, Mssql, MySQL, Mysql, Neo4J, Oracle,
    PostgreSQL, Postgresql, Scylla
from diagrams.onprem.dns import Coredns, Powerdns
from diagrams.onprem.etl import Embulk
from diagrams.onprem.gitops import ArgoCD, Argocd, Flagger, Flux
from diagrams.onprem.groupware import Nextcloud
from diagrams.onprem.iac import Ansible, Atlantis, Awx, Puppet, Terraform
from diagrams.onprem.identity import Dex
from diagrams.onprem.inmemory import Aerospike, Hazelcast, Memcached, Redis
from diagrams.onprem.logging import FluentBit, Fluentbit, Graylog, Loki, RSyslog, Rsyslog, SyslogNg
from diagrams.onprem.messaging import Centrifugo
from diagrams.onprem.mlops import Mlflow, Polyaxon
from diagrams.onprem.monitoring import Cortex, Datadog, Dynatrace, Grafana, Humio, Mimir, Nagios,
    Newrelic, Prometheus, PrometheusOperator, Sentry, Splunk, Thanos, Zabbix
from diagrams.onprem.network import Ambassador, Apache, Bind9, Caddy, Consul, ETCD, Envoy, Etcd,
    Glassfish, Gunicorn, HAProxy, Haproxy, Internet, Istio, Jbossas, Jetty, Kong, Linkerd, Nginx,
    OPNSense, OSM, Ocelot, OpenServiceMesh, Opnsense, PFSense, Pfsense, Pomerium, Powerdns, Tomcat,
    Traefik, Tyk, VyOS, Vyos, Wildfly, Yarp, Zookeeper
from diagrams.onprem.proxmox import ProxmoxVE, Pve
from diagrams.onprem.queue import ActiveMQ, Activemq, Celery, EMQX, Emqx, Kafka, Nats, RabbitMQ,
    Rabbitmq, ZeroMQ, Zeromq
from diagrams.onprem.registry import Harbor, Jfrog
from diagrams.onprem.search import Solr
from diagrams.onprem.security import Bitwarden, Trivy, Vault
from diagrams.onprem.storage import CEPH, CEPH_OSD, Ceph, CephOsd, Glusterfs, Portworx
from diagrams.onprem.tracing import Jaeger, Tempo
from diagrams.onprem.vcs import Git, Gitea, Github, Gitlab, Svn
from diagrams.onprem.workflow import Airflow, Digdag, KubeFlow, Kubeflow, NiFi, Nifi

# OPENSTACK
from diagrams.openstack.apiproxies import EC2API
from diagrams.openstack.applicationlifecycle import Freezer, Masakari, Murano, Solum
from diagrams.openstack.baremetal import Cyborg, Ironic
from diagrams.openstack.billing import CloudKitty, Cloudkitty
from diagrams.openstack.compute import Nova, Qinling, Zun
from diagrams.openstack.containerservices import Kuryr
from diagrams.openstack.deployment import Ansible, Charms, Chef, Helm, Kolla, KollaAnsible, TripleO,
    Tripleo
from diagrams.openstack.frontend import Horizon
from diagrams.openstack.monitoring import Monasca, Telemetry
from diagrams.openstack.multiregion import Tricircle
from diagrams.openstack.networking import Designate, Neutron, Octavia
from diagrams.openstack.nfv import Tacker
from diagrams.openstack.optimization import Congress, Rally, Vitrage, Watcher
from diagrams.openstack.orchestration import Blazar, Heat, Mistral, Senlin, Zaqar
from diagrams.openstack.packaging import LOCI, Puppet, RPM
from diagrams.openstack.sharedservices import Barbican, Glance, Karbor, Keystone, Searchlight
from diagrams.openstack.storage import Cinder, Manila, Swift
from diagrams.openstack.user import OpenStackClient, Openstackclient
from diagrams.openstack.workloadprovisioning import Magnum, Sahara, Trove

# OUTSCALE
from diagrams.outscale.compute import Compute, DirectConnect
from diagrams.outscale.network import ClientVpn, InternetService, LoadBalancer, NatService, Net,
    SiteToSiteVpng
from diagrams.outscale.security import Firewall, IdentityAndAccessManagement
from diagrams.outscale.storage import SimpleStorageService, Storage

# PROGRAMMING
from diagrams.programming.flowchart import Action, Collate, Database, Decision, Delay, Display,
    Document, InputOutput, Inspection, InternalStorage, LoopLimit, ManualInput, ManualLoop, Merge,
    MultipleDocuments, OffPageConnectorLeft, OffPageConnectorRight, Or, PredefinedProcess,
    Preparation, Sort, StartEnd, StoredData, SummingJunction
from diagrams.programming.framework import Angular, Backbone, Camel, Django, DotNet, Dotnet, Ember,
    FastAPI, Fastapi, Flask, Flutter, GraphQL, Graphql, Hibernate, JHipster, Jhipster, Laravel,
    Micronaut, NextJs, Nextjs, Quarkus, Rails, React, Spring, Starlette, Svelte, Vercel, Vue
from diagrams.programming.language import Bash, C, Cpp, Csharp, Dart, Elixir, Erlang, Go, Java,
    JavaScript, Javascript, Kotlin, Latex, Matlab, NodeJS, Nodejs, PHP, Php, Python, R, Ruby, Rust,
    Scala, Swift, TypeScript, Typescript
from diagrams.programming.runtime import Dapr

# SAAS
from diagrams.saas.alerting import Newrelic, Opsgenie, Pagerduty, Pushover, Xmatters
from diagrams.saas.analytics import Dataform, Snowflake, Stitch
from diagrams.saas.cdn import Akamai, Cloudflare, Fastly
from diagrams.saas.chat import Discord, Line, Mattermost, Messenger, RocketChat, Slack, Teams,
    Telegram
from diagrams.saas.communication import Twilio
from diagrams.saas.filesharing import Nextcloud
from diagrams.saas.identity import Auth0, Okta
from diagrams.saas.logging import DataDog, Datadog, NewRelic, Newrelic, Papertrail
from diagrams.saas.media import Cloudinary
from diagrams.saas.recommendation import Recombee
from diagrams.saas.security import Sonarqube
from diagrams.saas.social import Facebook, Twitter
