/*
Copyright 2024.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package main

import (
	"context"
	"encoding/json"

	"k8s.io/apimachinery/pkg/apis/meta/v1/unstructured"
	"sigs.k8s.io/yaml"

	// Import all Kubernetes client auth plugins (e.g. Azure, GCP, OIDC, etc.)
	// to ensure that exec-entrypoint and run can make use of them.
	_ "k8s.io/client-go/plugin/pkg/client/auth"

	"sigs.k8s.io/controller-runtime/pkg/client"
	"sigs.k8s.io/controller-runtime/pkg/client/config"
	//+kubebuilder:scaffold:imports
)

type KubeClient interface {
	Create(obj []byte) (error)
}
type kubeClientImpl struct {
	client client.Client
}

func (k kubeClientImpl) Create(rawObj []byte) error {
	parsedObj, err := ParseJSONToUnstructured(rawObj);
	if (err != nil){
		return err
	}
	err = k.client.Create(context.Background(), parsedObj);
	return err
}

func GetClient() (KubeClient, error) {
	cfg := config.GetConfigOrDie();
	cli, err := client.New(cfg, client.Options{});
	if (err != nil){
		return nil, err;
	}
	return kubeClientImpl{client: cli}, nil;
}

func ParseJSONToUnstructured(jsonData []byte) (*unstructured.Unstructured, error) {
	var obj map[string]interface{}
	if err := json.Unmarshal(jsonData, &obj); err != nil {
		return nil, err
	}

	yamlData, err := yaml.JSONToYAML(jsonData)
	if err != nil {
		return nil, err
	}

	u := &unstructured.Unstructured{}
	if err := u.UnmarshalJSON(yamlData); err != nil {
		return nil, err
	}

	return u, nil
}