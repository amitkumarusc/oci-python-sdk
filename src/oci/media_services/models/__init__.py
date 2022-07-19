# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .akamai_manual_stream_cdn_config import AkamaiManualStreamCdnConfig
from .asset_metadata_entry_details import AssetMetadataEntryDetails
from .change_media_asset_compartment_details import ChangeMediaAssetCompartmentDetails
from .change_media_workflow_compartment_details import ChangeMediaWorkflowCompartmentDetails
from .change_media_workflow_configuration_compartment_details import ChangeMediaWorkflowConfigurationCompartmentDetails
from .change_media_workflow_job_compartment_details import ChangeMediaWorkflowJobCompartmentDetails
from .change_stream_distribution_channel_compartment_details import ChangeStreamDistributionChannelCompartmentDetails
from .create_media_asset_details import CreateMediaAssetDetails
from .create_media_workflow_configuration_details import CreateMediaWorkflowConfigurationDetails
from .create_media_workflow_details import CreateMediaWorkflowDetails
from .create_media_workflow_job_by_id_details import CreateMediaWorkflowJobByIdDetails
from .create_media_workflow_job_by_name_details import CreateMediaWorkflowJobByNameDetails
from .create_media_workflow_job_details import CreateMediaWorkflowJobDetails
from .create_stream_cdn_config_details import CreateStreamCdnConfigDetails
from .create_stream_distribution_channel_details import CreateStreamDistributionChannelDetails
from .create_stream_packaging_config_details import CreateStreamPackagingConfigDetails
from .dash_stream_packaging_config import DashStreamPackagingConfig
from .edge_stream_cdn_config import EdgeStreamCdnConfig
from .hls_stream_packaging_config import HlsStreamPackagingConfig
from .ingest_stream_distribution_channel_details import IngestStreamDistributionChannelDetails
from .ingest_stream_distribution_channel_result import IngestStreamDistributionChannelResult
from .job_output import JobOutput
from .media_asset import MediaAsset
from .media_asset_collection import MediaAssetCollection
from .media_asset_distribution_channel_attachment import MediaAssetDistributionChannelAttachment
from .media_asset_distribution_channel_attachment_collection import MediaAssetDistributionChannelAttachmentCollection
from .media_asset_distribution_channel_attachment_summary import MediaAssetDistributionChannelAttachmentSummary
from .media_asset_summary import MediaAssetSummary
from .media_asset_tag import MediaAssetTag
from .media_workflow import MediaWorkflow
from .media_workflow_collection import MediaWorkflowCollection
from .media_workflow_configuration import MediaWorkflowConfiguration
from .media_workflow_configuration_collection import MediaWorkflowConfigurationCollection
from .media_workflow_configuration_summary import MediaWorkflowConfigurationSummary
from .media_workflow_job import MediaWorkflowJob
from .media_workflow_job_collection import MediaWorkflowJobCollection
from .media_workflow_job_fact import MediaWorkflowJobFact
from .media_workflow_job_fact_collection import MediaWorkflowJobFactCollection
from .media_workflow_job_fact_summary import MediaWorkflowJobFactSummary
from .media_workflow_job_summary import MediaWorkflowJobSummary
from .media_workflow_summary import MediaWorkflowSummary
from .media_workflow_task import MediaWorkflowTask
from .media_workflow_task_declaration import MediaWorkflowTaskDeclaration
from .media_workflow_task_declaration_collection import MediaWorkflowTaskDeclarationCollection
from .media_workflow_task_state import MediaWorkflowTaskState
from .metadata import Metadata
from .stream_cdn_config import StreamCdnConfig
from .stream_cdn_config_collection import StreamCdnConfigCollection
from .stream_cdn_config_section import StreamCdnConfigSection
from .stream_cdn_config_summary import StreamCdnConfigSummary
from .stream_distribution_channel import StreamDistributionChannel
from .stream_distribution_channel_collection import StreamDistributionChannelCollection
from .stream_distribution_channel_summary import StreamDistributionChannelSummary
from .stream_packaging_config import StreamPackagingConfig
from .stream_packaging_config_collection import StreamPackagingConfigCollection
from .stream_packaging_config_encryption import StreamPackagingConfigEncryption
from .stream_packaging_config_encryption_aes128 import StreamPackagingConfigEncryptionAes128
from .stream_packaging_config_encryption_none import StreamPackagingConfigEncryptionNone
from .stream_packaging_config_summary import StreamPackagingConfigSummary
from .system_media_workflow import SystemMediaWorkflow
from .system_media_workflow_collection import SystemMediaWorkflowCollection
from .update_media_asset_details import UpdateMediaAssetDetails
from .update_media_workflow_configuration_details import UpdateMediaWorkflowConfigurationDetails
from .update_media_workflow_details import UpdateMediaWorkflowDetails
from .update_media_workflow_job_details import UpdateMediaWorkflowJobDetails
from .update_stream_cdn_config_details import UpdateStreamCdnConfigDetails
from .update_stream_distribution_channel_details import UpdateStreamDistributionChannelDetails
from .update_stream_packaging_config_details import UpdateStreamPackagingConfigDetails

# Maps type names to classes for media_services services.
media_services_type_mapping = {
    "AkamaiManualStreamCdnConfig": AkamaiManualStreamCdnConfig,
    "AssetMetadataEntryDetails": AssetMetadataEntryDetails,
    "ChangeMediaAssetCompartmentDetails": ChangeMediaAssetCompartmentDetails,
    "ChangeMediaWorkflowCompartmentDetails": ChangeMediaWorkflowCompartmentDetails,
    "ChangeMediaWorkflowConfigurationCompartmentDetails": ChangeMediaWorkflowConfigurationCompartmentDetails,
    "ChangeMediaWorkflowJobCompartmentDetails": ChangeMediaWorkflowJobCompartmentDetails,
    "ChangeStreamDistributionChannelCompartmentDetails": ChangeStreamDistributionChannelCompartmentDetails,
    "CreateMediaAssetDetails": CreateMediaAssetDetails,
    "CreateMediaWorkflowConfigurationDetails": CreateMediaWorkflowConfigurationDetails,
    "CreateMediaWorkflowDetails": CreateMediaWorkflowDetails,
    "CreateMediaWorkflowJobByIdDetails": CreateMediaWorkflowJobByIdDetails,
    "CreateMediaWorkflowJobByNameDetails": CreateMediaWorkflowJobByNameDetails,
    "CreateMediaWorkflowJobDetails": CreateMediaWorkflowJobDetails,
    "CreateStreamCdnConfigDetails": CreateStreamCdnConfigDetails,
    "CreateStreamDistributionChannelDetails": CreateStreamDistributionChannelDetails,
    "CreateStreamPackagingConfigDetails": CreateStreamPackagingConfigDetails,
    "DashStreamPackagingConfig": DashStreamPackagingConfig,
    "EdgeStreamCdnConfig": EdgeStreamCdnConfig,
    "HlsStreamPackagingConfig": HlsStreamPackagingConfig,
    "IngestStreamDistributionChannelDetails": IngestStreamDistributionChannelDetails,
    "IngestStreamDistributionChannelResult": IngestStreamDistributionChannelResult,
    "JobOutput": JobOutput,
    "MediaAsset": MediaAsset,
    "MediaAssetCollection": MediaAssetCollection,
    "MediaAssetDistributionChannelAttachment": MediaAssetDistributionChannelAttachment,
    "MediaAssetDistributionChannelAttachmentCollection": MediaAssetDistributionChannelAttachmentCollection,
    "MediaAssetDistributionChannelAttachmentSummary": MediaAssetDistributionChannelAttachmentSummary,
    "MediaAssetSummary": MediaAssetSummary,
    "MediaAssetTag": MediaAssetTag,
    "MediaWorkflow": MediaWorkflow,
    "MediaWorkflowCollection": MediaWorkflowCollection,
    "MediaWorkflowConfiguration": MediaWorkflowConfiguration,
    "MediaWorkflowConfigurationCollection": MediaWorkflowConfigurationCollection,
    "MediaWorkflowConfigurationSummary": MediaWorkflowConfigurationSummary,
    "MediaWorkflowJob": MediaWorkflowJob,
    "MediaWorkflowJobCollection": MediaWorkflowJobCollection,
    "MediaWorkflowJobFact": MediaWorkflowJobFact,
    "MediaWorkflowJobFactCollection": MediaWorkflowJobFactCollection,
    "MediaWorkflowJobFactSummary": MediaWorkflowJobFactSummary,
    "MediaWorkflowJobSummary": MediaWorkflowJobSummary,
    "MediaWorkflowSummary": MediaWorkflowSummary,
    "MediaWorkflowTask": MediaWorkflowTask,
    "MediaWorkflowTaskDeclaration": MediaWorkflowTaskDeclaration,
    "MediaWorkflowTaskDeclarationCollection": MediaWorkflowTaskDeclarationCollection,
    "MediaWorkflowTaskState": MediaWorkflowTaskState,
    "Metadata": Metadata,
    "StreamCdnConfig": StreamCdnConfig,
    "StreamCdnConfigCollection": StreamCdnConfigCollection,
    "StreamCdnConfigSection": StreamCdnConfigSection,
    "StreamCdnConfigSummary": StreamCdnConfigSummary,
    "StreamDistributionChannel": StreamDistributionChannel,
    "StreamDistributionChannelCollection": StreamDistributionChannelCollection,
    "StreamDistributionChannelSummary": StreamDistributionChannelSummary,
    "StreamPackagingConfig": StreamPackagingConfig,
    "StreamPackagingConfigCollection": StreamPackagingConfigCollection,
    "StreamPackagingConfigEncryption": StreamPackagingConfigEncryption,
    "StreamPackagingConfigEncryptionAes128": StreamPackagingConfigEncryptionAes128,
    "StreamPackagingConfigEncryptionNone": StreamPackagingConfigEncryptionNone,
    "StreamPackagingConfigSummary": StreamPackagingConfigSummary,
    "SystemMediaWorkflow": SystemMediaWorkflow,
    "SystemMediaWorkflowCollection": SystemMediaWorkflowCollection,
    "UpdateMediaAssetDetails": UpdateMediaAssetDetails,
    "UpdateMediaWorkflowConfigurationDetails": UpdateMediaWorkflowConfigurationDetails,
    "UpdateMediaWorkflowDetails": UpdateMediaWorkflowDetails,
    "UpdateMediaWorkflowJobDetails": UpdateMediaWorkflowJobDetails,
    "UpdateStreamCdnConfigDetails": UpdateStreamCdnConfigDetails,
    "UpdateStreamDistributionChannelDetails": UpdateStreamDistributionChannelDetails,
    "UpdateStreamPackagingConfigDetails": UpdateStreamPackagingConfigDetails
}
