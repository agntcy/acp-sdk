Module agntcy_acp.agws_v0.models
================================

Classes
-------

`Agent(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: uuid.UUID`
    :   The type of the None singleton.

    `metadata: agntcy_acp.agws_v0.models.AgentMetadata`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

`AgentACPDescriptor(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `metadata: agntcy_acp.agws_v0.models.AgentMetadata`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `specs: agntcy_acp.agws_v0.models.AgentACPSpec`
    :   The type of the None singleton.

`AgentACPSpec(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `capabilities: agntcy_acp.agws_v0.models.Capabilities`
    :   The type of the None singleton.

    `config: Dict[str, Any]`
    :   The type of the None singleton.

    `custom_streaming_update: Dict[str, Any] | None`
    :   The type of the None singleton.

    `input: Dict[str, Any]`
    :   The type of the None singleton.

    `interrupts: List[agntcy_acp.agws_v0.models.Interrupt] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `output: Dict[str, Any]`
    :   The type of the None singleton.

    `thread_state: Dict[str, Any] | None`
    :   The type of the None singleton.

`AgentACPSpecModel(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `capabilities: agntcy_acp.agws_v0.models.Capabilities1`
    :   The type of the None singleton.

    `config: Dict[str, Any]`
    :   The type of the None singleton.

    `custom_streaming_update: Dict[str, Any] | None`
    :   The type of the None singleton.

    `input: Dict[str, Any]`
    :   The type of the None singleton.

    `interrupts: List[agntcy_acp.agws_v0.models.Interrupt] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `output: Dict[str, Any]`
    :   The type of the None singleton.

    `thread_state: Dict[str, Any] | None`
    :   The type of the None singleton.

`AgentConnectProtocol(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: uuid.UUID | None`
    :   The type of the None singleton.

    `authentication: agntcy_acp.agws_v0.models.SecurityScheme | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `type: agntcy_acp.agws_v0.models.Type12`
    :   The type of the None singleton.

    `url: pydantic.networks.AnyUrl`
    :   The type of the None singleton.

`AgentDependency(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `deployment_option: str | None`
    :   The type of the None singleton.

    `env_var_values: agntcy_acp.agws_v0.models.EnvVarValues | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `name: str`
    :   The type of the None singleton.

    `ref: agntcy_acp.agws_v0.models.AgentRefModel`
    :   The type of the None singleton.

`AgentDeployment(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `dependencies: List[agntcy_acp.agws_v0.models.AgentDependency] | None`
    :   The type of the None singleton.

    `deployment_options: List[agntcy_acp.agws_v0.models.DeploymentOptions]`
    :   The type of the None singleton.

    `env_vars: List[agntcy_acp.agws_v0.models.EnvVar] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

`AgentManifest(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `deployment: agntcy_acp.agws_v0.models.AgentDeployment | None`
    :   The type of the None singleton.

    `metadata: agntcy_acp.agws_v0.models.AgentMetadata`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `specs: agntcy_acp.agws_v0.models.AgentACPSpec`
    :   The type of the None singleton.

`AgentMetadata(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `description: str`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `ref: agntcy_acp.agws_v0.models.AgentRefModel`
    :   The type of the None singleton.

`AgentRef(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `name: str`
    :   The type of the None singleton.

    `url: pydantic.networks.AnyUrl | None`
    :   The type of the None singleton.

    `version: str`
    :   The type of the None singleton.

`AgentRefModel(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `name: str`
    :   The type of the None singleton.

    `url: pydantic.networks.AnyUrl | None`
    :   The type of the None singleton.

    `version: str`
    :   The type of the None singleton.

`AgentSearchRequest(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `limit: int | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `name: str | None`
    :   The type of the None singleton.

    `offset: int | None`
    :   The type of the None singleton.

    `version: str | None`
    :   The type of the None singleton.

`Capabilities(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `callbacks: bool | None`
    :   The type of the None singleton.

    `interrupts: bool | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `streaming: agntcy_acp.agws_v0.models.Streaming | None`
    :   The type of the None singleton.

    `threads: bool | None`
    :   The type of the None singleton.

`Capabilities1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `callbacks: bool | None`
    :   The type of the None singleton.

    `interrupts: bool | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `streaming: agntcy_acp.agws_v0.models.Streaming1 | None`
    :   The type of the None singleton.

    `threads: bool | None`
    :   The type of the None singleton.

`Config(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `configurable: agntcy_acp.agws_v0.models.ConfigSchema | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `recursion_limit: int | None`
    :   The type of the None singleton.

    `tags: List[str] | None`
    :   The type of the None singleton.

`ConfigSchema(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

`Content(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `text: str`
    :   The type of the None singleton.

    `type: Literal['text']`
    :   The type of the None singleton.

`Content1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `type: str`
    :   The type of the None singleton.

`CustomRunResultUpdate(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID | None`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus`
    :   The type of the None singleton.

    `type: Literal['custom']`
    :   The type of the None singleton.

    `update: agntcy_acp.agws_v0.models.StreamUpdateSchema`
    :   The type of the None singleton.

`CustomRunResultUpdateModel(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus`
    :   The type of the None singleton.

    `type: Literal['custom']`
    :   The type of the None singleton.

    `update: agntcy_acp.agws_v0.models.StreamUpdateSchema`
    :   The type of the None singleton.

`DeploymentOptions(root: RootModelRootType = PydanticUndefined, **data)`
:   !!! abstract "Usage Documentation"
        [`RootModel` and Custom Root Types](../concepts/models.md#rootmodel-and-custom-root-types)
    
    A Pydantic `BaseModel` for the root object of the model.
    
    Attributes:
        root: The root object of the model.
        __pydantic_root_model__: Whether the model is a RootModel.
        __pydantic_private__: Private fields in the model.
        __pydantic_extra__: Extra fields in the model.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.root_model.RootModel[Union[SourceCodeDeployment, RemoteServiceDeployment, DockerDeployment]]
    * pydantic.root_model.RootModel
    * pydantic.main.BaseModel
    * typing.Generic

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `root: agntcy_acp.agws_v0.models.SourceCodeDeployment | agntcy_acp.agws_v0.models.RemoteServiceDeployment | agntcy_acp.agws_v0.models.DockerDeployment`
    :   The type of the None singleton.

`DockerDeployment(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `image: pydantic.networks.AnyUrl`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `name: str | None`
    :   The type of the None singleton.

    `type: Literal['docker']`
    :   The type of the None singleton.

`EnvVar(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `defaultValue: str | None`
    :   The type of the None singleton.

    `desc: str`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `name: str`
    :   The type of the None singleton.

    `required: bool | None`
    :   The type of the None singleton.

`EnvVarValues(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `dependencies: List[agntcy_acp.agws_v0.models.EnvVarValues] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `name: str | None`
    :   The type of the None singleton.

    `values: Dict[str, str] | None`
    :   The type of the None singleton.

`ErrorResponse(root: RootModelRootType = PydanticUndefined, **data)`
:   !!! abstract "Usage Documentation"
        [`RootModel` and Custom Root Types](../concepts/models.md#rootmodel-and-custom-root-types)
    
    A Pydantic `BaseModel` for the root object of the model.
    
    Attributes:
        root: The root object of the model.
        __pydantic_root_model__: Whether the model is a RootModel.
        __pydantic_private__: Private fields in the model.
        __pydantic_extra__: Extra fields in the model.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.root_model.RootModel[str]
    * pydantic.root_model.RootModel
    * pydantic.main.BaseModel
    * typing.Generic

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `root: str`
    :   The type of the None singleton.

`Event(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `agent_event`
    :   The type of the None singleton.

`FrameworkType(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `langgraph`
    :   The type of the None singleton.

`FrameworkType1(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `llamaindex`
    :   The type of the None singleton.

`IfExists(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `do_nothing`
    :   The type of the None singleton.

    `raise_`
    :   The type of the None singleton.

`IfNotExists(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `create`
    :   The type of the None singleton.

    `reject`
    :   The type of the None singleton.

`InputSchema(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

`Interrupt(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `interrupt_payload: Dict[str, Any]`
    :   The type of the None singleton.

    `interrupt_type: str`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `resume_payload: Dict[str, Any]`
    :   The type of the None singleton.

`InterruptPayloadSchema(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

`LangGraphConfig(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `framework_type: Literal['langgraph']`
    :   The type of the None singleton.

    `graph: str`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

`LlamaIndexConfig(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `framework_type: Literal['llamaindex']`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `path: str`
    :   The type of the None singleton.

`Message(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `content: str | List[agntcy_acp.agws_v0.models.Content | agntcy_acp.agws_v0.models.Content1]`
    :   The type of the None singleton.

    `id: str | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `role: str`
    :   The type of the None singleton.

`MultitaskStrategy(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `enqueue`
    :   The type of the None singleton.

    `interrupt`
    :   The type of the None singleton.

    `reject`
    :   The type of the None singleton.

    `rollback`
    :   The type of the None singleton.

`OnCompletion(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `delete`
    :   The type of the None singleton.

    `keep`
    :   The type of the None singleton.

`OnDisconnect(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `cancel`
    :   The type of the None singleton.

    `continue_`
    :   The type of the None singleton.

`OutputSchema(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

`RemoteServiceDeployment(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `name: str | None`
    :   The type of the None singleton.

    `protocol: agntcy_acp.agws_v0.models.AgentConnectProtocol`
    :   The type of the None singleton.

    `type: Literal['remote_service']`
    :   The type of the None singleton.

`ResumePayloadSchema(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

`Run(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Descendants

    * agntcy_acp.agws_v0.models.RunStateful
    * agntcy_acp.agws_v0.models.RunStateless

    ### Class variables

    `agent_id: uuid.UUID`
    :   The type of the None singleton.

    `created_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus`
    :   The type of the None singleton.

    `thread_id: uuid.UUID | None`
    :   The type of the None singleton.

    `updated_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

`Run1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: uuid.UUID`
    :   The type of the None singleton.

    `created_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

    `creation: agntcy_acp.agws_v0.models.RunCreate1`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus`
    :   The type of the None singleton.

    `thread_id: uuid.UUID | None`
    :   The type of the None singleton.

    `updated_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

`RunCreate(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Descendants

    * agntcy_acp.agws_v0.models.RunCreateStateful
    * agntcy_acp.agws_v0.models.RunCreateStateless

    ### Class variables

    `after_seconds: int | None`
    :   The type of the None singleton.

    `agent_id: str | None`
    :   The type of the None singleton.

    `config: agntcy_acp.agws_v0.models.Config | None`
    :   The type of the None singleton.

    `input: agntcy_acp.agws_v0.models.InputSchema | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `multitask_strategy: agntcy_acp.agws_v0.models.MultitaskStrategy | None`
    :   The type of the None singleton.

    `on_disconnect: agntcy_acp.agws_v0.models.OnDisconnect | None`
    :   The type of the None singleton.

    `stream_mode: List[agntcy_acp.agws_v0.models.StreamingMode] | agntcy_acp.agws_v0.models.StreamingMode | None`
    :   The type of the None singleton.

    `webhook: pydantic.networks.AnyUrl | None`
    :   The type of the None singleton.

`RunCreate1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: uuid.UUID`
    :   The type of the None singleton.

    `config: agntcy_acp.agws_v0.models.ConfigSchema | None`
    :   The type of the None singleton.

    `input: agntcy_acp.agws_v0.models.InputSchema | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `streaming: agntcy_acp.agws_v0.models.StreamingModeModel | None`
    :   The type of the None singleton.

    `thread_id: uuid.UUID | None`
    :   The type of the None singleton.

    `webhook: pydantic.networks.AnyUrl | None`
    :   The type of the None singleton.

`RunCreateStateful(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * agntcy_acp.agws_v0.models.RunCreate
    * pydantic.main.BaseModel

    ### Class variables

    `after_seconds: int | None`
    :   The type of the None singleton.

    `agent_id: str | None`
    :   The type of the None singleton.

    `config: agntcy_acp.agws_v0.models.Config | None`
    :   The type of the None singleton.

    `if_not_exists: agntcy_acp.agws_v0.models.IfNotExists | None`
    :   The type of the None singleton.

    `input: agntcy_acp.agws_v0.models.InputSchema | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `multitask_strategy: agntcy_acp.agws_v0.models.MultitaskStrategy | None`
    :   The type of the None singleton.

    `on_disconnect: agntcy_acp.agws_v0.models.OnDisconnect | None`
    :   The type of the None singleton.

    `stream_mode: List[agntcy_acp.agws_v0.models.StreamingMode] | agntcy_acp.agws_v0.models.StreamingMode | None`
    :   The type of the None singleton.

    `stream_subgraphs: bool | None`
    :   The type of the None singleton.

    `webhook: pydantic.networks.AnyUrl | None`
    :   The type of the None singleton.

`RunCreateStateless(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * agntcy_acp.agws_v0.models.RunCreate
    * pydantic.main.BaseModel

    ### Class variables

    `after_seconds: int | None`
    :   The type of the None singleton.

    `agent_id: str | None`
    :   The type of the None singleton.

    `config: agntcy_acp.agws_v0.models.Config | None`
    :   The type of the None singleton.

    `input: agntcy_acp.agws_v0.models.InputSchema | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `multitask_strategy: agntcy_acp.agws_v0.models.MultitaskStrategy | None`
    :   The type of the None singleton.

    `on_completion: agntcy_acp.agws_v0.models.OnCompletion | None`
    :   The type of the None singleton.

    `on_disconnect: agntcy_acp.agws_v0.models.OnDisconnect | None`
    :   The type of the None singleton.

    `stream_mode: List[agntcy_acp.agws_v0.models.StreamingMode] | agntcy_acp.agws_v0.models.StreamingMode | None`
    :   The type of the None singleton.

    `webhook: pydantic.networks.AnyUrl | None`
    :   The type of the None singleton.

`RunError(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `description: str`
    :   The type of the None singleton.

    `errcode: int`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `type: Literal['error']`
    :   The type of the None singleton.

`RunErrorModel(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `description: str`
    :   The type of the None singleton.

    `errcode: int`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `type: agntcy_acp.agws_v0.models.Type7`
    :   The type of the None singleton.

`RunInterrupt(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `interrupt: agntcy_acp.agws_v0.models.InterruptPayloadSchema`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `type: Literal['interrupt']`
    :   The type of the None singleton.

`RunInterruptModel(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `interrupt: agntcy_acp.agws_v0.models.InterruptPayloadSchema`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `type: agntcy_acp.agws_v0.models.Type8`
    :   The type of the None singleton.

`RunOutput(root: RootModelRootType = PydanticUndefined, **data)`
:   !!! abstract "Usage Documentation"
        [`RootModel` and Custom Root Types](../concepts/models.md#rootmodel-and-custom-root-types)
    
    A Pydantic `BaseModel` for the root object of the model.
    
    Attributes:
        root: The root object of the model.
        __pydantic_root_model__: Whether the model is a RootModel.
        __pydantic_private__: Private fields in the model.
        __pydantic_extra__: Extra fields in the model.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.root_model.RootModel[Union[RunResult, RunInterrupt, RunError]]
    * pydantic.root_model.RootModel
    * pydantic.main.BaseModel
    * typing.Generic

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `root: agntcy_acp.agws_v0.models.RunResult | agntcy_acp.agws_v0.models.RunInterrupt | agntcy_acp.agws_v0.models.RunError`
    :   The type of the None singleton.

`RunOutputStream(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `data: agntcy_acp.agws_v0.models.ValueRunResultUpdate | agntcy_acp.agws_v0.models.CustomRunResultUpdate`
    :   The type of the None singleton.

    `event: agntcy_acp.agws_v0.models.Event`
    :   The type of the None singleton.

    `id: str`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

`RunOutputStream1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `data: agntcy_acp.agws_v0.models.RunResultModel | agntcy_acp.agws_v0.models.CustomRunResultUpdateModel`
    :   The type of the None singleton.

    `event: agntcy_acp.agws_v0.models.Event`
    :   The type of the None singleton.

    `id: str`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

`RunResult(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `messages: List[agntcy_acp.agws_v0.models.Message] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `type: Literal['result']`
    :   The type of the None singleton.

    `values: agntcy_acp.agws_v0.models.OutputSchema | None`
    :   The type of the None singleton.

`RunResultModel(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `result: agntcy_acp.agws_v0.models.OutputSchema`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus`
    :   The type of the None singleton.

    `type: Literal['result']`
    :   The type of the None singleton.

`RunSearchRequest(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: uuid.UUID | None`
    :   The type of the None singleton.

    `limit: int | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `offset: int | None`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus | None`
    :   The type of the None singleton.

`RunStateful(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * agntcy_acp.agws_v0.models.Run
    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: uuid.UUID`
    :   The type of the None singleton.

    `created_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

    `creation: agntcy_acp.agws_v0.models.RunCreateStateful`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus`
    :   The type of the None singleton.

    `thread_id: uuid.UUID | None`
    :   The type of the None singleton.

    `updated_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

`RunStateless(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * agntcy_acp.agws_v0.models.Run
    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: uuid.UUID`
    :   The type of the None singleton.

    `created_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

    `creation: agntcy_acp.agws_v0.models.RunCreateStateless`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus`
    :   The type of the None singleton.

    `thread_id: uuid.UUID | None`
    :   The type of the None singleton.

    `updated_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

`RunStatus(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `error`
    :   The type of the None singleton.

    `interrupted`
    :   The type of the None singleton.

    `pending`
    :   The type of the None singleton.

    `success`
    :   The type of the None singleton.

    `timeout`
    :   The type of the None singleton.

`RunWaitResponseStateful(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `output: agntcy_acp.agws_v0.models.RunOutput | None`
    :   The type of the None singleton.

    `run: agntcy_acp.agws_v0.models.RunStateful | None`
    :   The type of the None singleton.

`RunWaitResponseStateless(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    `output: agntcy_acp.agws_v0.models.RunOutput | None`
    :   The type of the None singleton.

    `run: agntcy_acp.agws_v0.models.RunStateless | None`
    :   The type of the None singleton.

`SecurityScheme(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

`SourceCodeDeployment(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `framework_config: agntcy_acp.agws_v0.models.LangGraphConfig | agntcy_acp.agws_v0.models.LlamaIndexConfig`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `name: str | None`
    :   The type of the None singleton.

    `type: Literal['source_code']`
    :   The type of the None singleton.

    `url: pydantic.networks.AnyUrl`
    :   The type of the None singleton.

`Status(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `busy`
    :   The type of the None singleton.

    `error`
    :   The type of the None singleton.

    `idle`
    :   The type of the None singleton.

    `interrupted`
    :   The type of the None singleton.

`StreamUpdateSchema(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

`Streaming(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `custom: bool | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `values: bool | None`
    :   The type of the None singleton.

`Streaming1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `custom: bool | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `result: bool | None`
    :   The type of the None singleton.

`StreamingMode(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `custom`
    :   The type of the None singleton.

    `values`
    :   The type of the None singleton.

`StreamingModeModel(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `custom`
    :   The type of the None singleton.

    `result`
    :   The type of the None singleton.

`Thread(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `created_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

    `messages: List[agntcy_acp.agws_v0.models.Message] | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any]`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.Status`
    :   The type of the None singleton.

    `thread_id: str`
    :   The type of the None singleton.

    `updated_at: pydantic.types.AwareDatetime`
    :   The type of the None singleton.

    `values: agntcy_acp.agws_v0.models.ThreadStateSchema | None`
    :   The type of the None singleton.

`Thread1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: str`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `thread_id: str`
    :   The type of the None singleton.

`ThreadCheckpoint(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `checkpoint_id: uuid.UUID`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

`ThreadCreate(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `if_exists: agntcy_acp.agws_v0.models.IfExists | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `thread_id: uuid.UUID | None`
    :   The type of the None singleton.

`ThreadCreate1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: str`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

`ThreadPatch(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `checkpoint: agntcy_acp.agws_v0.models.ThreadCheckpoint | None`
    :   The type of the None singleton.

    `messages: List[agntcy_acp.agws_v0.models.Message] | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `values: agntcy_acp.agws_v0.models.ThreadStateSchema | None`
    :   The type of the None singleton.

`ThreadSearchRequest(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `limit: int | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `offset: int | None`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.ThreadStatus | None`
    :   The type of the None singleton.

    `values: Dict[str, Any] | None`
    :   The type of the None singleton.

`ThreadSearchRequest1(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `agent_id: uuid.UUID | None`
    :   The type of the None singleton.

    `limit: int | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `offset: int | None`
    :   The type of the None singleton.

`ThreadState(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `checkpoint: agntcy_acp.agws_v0.models.ThreadCheckpoint`
    :   The type of the None singleton.

    `messages: List[agntcy_acp.agws_v0.models.Message] | None`
    :   The type of the None singleton.

    `metadata: Dict[str, Any] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `values: agntcy_acp.agws_v0.models.ThreadStateSchema`
    :   The type of the None singleton.

`ThreadStateSchema(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

`ThreadStatus(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `busy`
    :   The type of the None singleton.

    `error`
    :   The type of the None singleton.

    `idle`
    :   The type of the None singleton.

    `interrupted`
    :   The type of the None singleton.

`Type(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `result`
    :   The type of the None singleton.

`Type1(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `values`
    :   The type of the None singleton.

`Type10(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `remote_service`
    :   The type of the None singleton.

`Type11(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `docker`
    :   The type of the None singleton.

`Type12(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `ACP`
    :   The type of the None singleton.

`Type2(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `custom`
    :   The type of the None singleton.

`Type3(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `error`
    :   The type of the None singleton.

`Type4(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `interrupt`
    :   The type of the None singleton.

`Type5(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `result`
    :   The type of the None singleton.

`Type6(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `custom`
    :   The type of the None singleton.

`Type7(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `error`
    :   The type of the None singleton.

`Type8(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `interrupt`
    :   The type of the None singleton.

`Type9(*args, **kwds)`
:   Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `source_code`
    :   The type of the None singleton.

`ValueRunResultUpdate(**data: Any)`
:   !!! abstract "Usage Documentation"
        [Models](../concepts/models.md)
    
    A base class for creating Pydantic models.
    
    Attributes:
        __class_vars__: The names of the class variables defined on the model.
        __private_attributes__: Metadata about the private attributes of the model.
        __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
    
        __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
        __pydantic_core_schema__: The core schema of the model.
        __pydantic_custom_init__: Whether the model has a custom `__init__` function.
        __pydantic_decorators__: Metadata containing the decorators defined on the model.
            This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
        __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
            __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
        __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
        __pydantic_post_init__: The name of the post-init method for the model, if defined.
        __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
        __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
        __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.
    
        __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
        __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
    
        __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
            is set to `'allow'`.
        __pydantic_fields_set__: The names of fields explicitly set during instantiation.
        __pydantic_private__: Values of private attributes set on the model instance.
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel

    ### Class variables

    `messages: List[agntcy_acp.agws_v0.models.Message] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `run_id: uuid.UUID`
    :   The type of the None singleton.

    `status: agntcy_acp.agws_v0.models.RunStatus`
    :   The type of the None singleton.

    `type: Literal['values']`
    :   The type of the None singleton.

    `values: agntcy_acp.agws_v0.models.OutputSchema`
    :   The type of the None singleton.